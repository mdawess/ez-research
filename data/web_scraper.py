import re
from typing import List
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class Scraper:

    def __init__(self, blacklist: List[str] = None, unecessary_words: List[str] = None):
        """Initializes the class with a list of blacklisted words and unecessary words. """
        if not blacklist:
            self.blacklist = [
                "[document]",
                "noscript",
                "header",
                "html",
                "meta",
                "head",
                "input",
                "script",
                "style",
                "title",
                "h1",
                "h2",
                "h3",
                "h4",
                "\n",
                "(",
                ")",
            ]
        if not unecessary_words:
            self.unecessary_words = [
                "about us",
                "contact us",
                "privacy policy",
                "terms of use",
                "copyright",
                "tags",
                "photo",
                "credit",
                "copyright",
                "all rights reserved",
                "posted",
                "bssl",
                "search",
                "google analytics",
                "code of conduct",
                "accessibility policy",
            ]

    def get_website_text(
        self,
        url: str,
        ) -> str:
        """
        Returns a list of all the text on a website filtered to eliminate 
        blacklisted and unecessary words.
        """
        hdr = {
            "User-Agent": 
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        }
        req = Request(url, headers=hdr)
        website = urlopen(req)
        soup = BeautifulSoup(website, "html.parser")
        website_text = soup.findAll(text=True)
        output = ""
        list_output = []

        for t in website_text:
            if (
                t.parent.name not in self.blacklist
                and len(t) > 1
                and not any(word in t.lower() for word in self.unecessary_words)
            ):
                output += "{} ".format(t)
                list_output.append(t)

        return self.format_output(output)


    def format_output(self, output: str) -> str:
        """
        Formats the output to remove extra spaces and newlines
        so the ai can read the text better. Then adds a newline
        with TLDR to incite the summary generation.
        """
        sub_texts = round(len(output) % 1024, 0)
        output_list = []
        for i in range(sub_texts):
            output_list.append(output[sub_texts * i : sub_texts * (i + 1)])

        formatted_output = re.sub("\s+", " ", output)
        return formatted_output + "\n\nTLDR:"


if __name__ == "__main__":
    # Interesting lecture I read recently
    scraper = TLDRScraper()
    print(
        scraper.get_website_text(
            "http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html?curius=1466"
        )
    )
