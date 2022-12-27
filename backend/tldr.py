import requests
import sys, os
import openai
from serpapi import GoogleSearch
import psycopg2 as pg
from node import Node

class TLDR:

    def __init__(self) -> None:
        """Initialize the class"""
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        self.conn = pg.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS")
        )

    def _search(self, query: str) -> list:
        """Search the query on Google and return the top 5 results"""
        search = GoogleSearch({
            "q": query, 
            "api_key": os.environ.get("SERP_API_KEY"),
            "logging": False
        })
        result = search.get_dict()
        return list(map(result['link'], result['organic_results']))

    def _scrape_webpage(self, url: str) -> str:
        """Scrape the webpage for the article"""
        payload = {
            "url": url,
            "elements": [{"selector": "body"}]
        }
        resp = requests.post('https://chrome.browserless.io/scrape', 
            params={"token": os.environ.get("BROWSERLESS_API_KEY")}, 
            headers={'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}, 
            json=payload
        )
        webpage_text = resp.json()['data'][0]['results'][0]['text']
        return webpage_text


    def _summarize(self, query:str, text: str) -> str:
        """Summarize the article"""
        prompt = """
        The following text is a search result from the question {0}.

        {1}

        TLDR:
        """.format(query, text)
        tldr = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.9,
            max_tokens=800
        )
        return tldr.choices[0].text

    def _adjust_weights(self, node: Node, delta: float = 3) -> None:
        """Adjust the weights of the links of the node
        
        Currently, it just looks at the similarity of the title
        """
        cur = self.conn.cursor()
        query = """
            SELECT * FROM TLDR
            WHERE similarity(title, %s) > 0.8;
        """
        cur.execute(query, node.title)
        connection = cur.fetchone()
        if connection is not None:
            for i in range(len(node.links)):
                query = """
                    INSERT INTO CONNECTIONS (main_id, connected_id, weight)
                    VALUES (%s, %s, %s);
                """
                cur.execute(query, (node.id, connection[0], delta))
                self.conn.commit()
                delta -= 1
        cur.close()

    def tldr(self, query: str, num_links: int = 3):
        """Create a node for the query and tldr"""
        relevant_links = self._search(query)

        summaries = []
        for link in relevant_links[:num_links]:
            webpage_text = self._scrape_webpage(link)
            summary = self._summarize(query, webpage_text)
            summaries.append(summary)
        
        final_prompt = """
        Summarize the relevant info from the following {0} pieces of info: 
        """.format(num_links)
        for summary in summaries:
            final_prompt += "\n" + summary + "\n"

        final_prompt += "\nTLDR:"

        tldr = openai.Completion.create(
            engine="davinci",
            prompt=final_prompt,
            temperature=0.9,
            max_tokens=800
        )

        node = Node(query, tldr)
        cur = self.conn.cursor()
        query = """
                INSERT INTO TLDR (title, tldr) 
                VALUES (%s, %s) RETURNING tldr_id;
        """
        cur.execute(query, (node.title, node.tldr))
        node.node_id = cur.fetchone()[0]

        self._adjust_weights(node, delta=num_links)

        cur.close()
        return tldr.choices[0].text

    # Helper Methods for the db
    def _get_tldrs(self) -> dict:
        """Get the tldr from the database"""
        cur = self.conn.cursor()
        query = """
            SELECT * FROM TLDR;
        """
        cur.execute(query)
        tldr = cur.fetchone()
        tldrs = {}
        while tldr is not None:
            tldrs[tldr[0]] = Node(tldr[1], tldr[2])
            cur.fetchone()
        cur.close()
        return tldrs
    
    def _get_connections(self, main_id: int) -> dict:
        """Get the connections from the database where the main
        id is main_id"""
        cur = self.conn.cursor()
        query = """
            SELECT * FROM CONNECTIONS
            WHERE main_id = %s;
        """
        cur.execute(query, main_id)
        connection = cur.fetchone()
        connections = {}
        while connection is not None:
            connections[connection[1]] = []
            connections[connection[1]].append(connection[2])
            connection = cur.fetchone()
        cur.close()
        return connections

if __name__ == "__main__":
    tldr = TLDR()
    tldr.tldr("What is the meaning of life?")
        