import requests
import os
from typing import Dict, Tuple

class Search:

    def __init__(self, api_key: str, cx: str, url: str):
        """Initializes the class with the API key, CX and URL."""

        self.api_key = api_key
        self.cx = cx
        self.url = url

    def custom_search(self, query: str) -> Tuple[Dict[str, str], float]:
        """
        Custom search function using the custom search API.

        inputs will always take the form of:
            <{"key": api_key, "cx": cx, "q": query, "start": start}>
        where query is the search query and start is the start index, usually 1.
        """
        response = requests.get(self.url, params={
            "key": self.api_key, 
            "cx": self.api_key, 
            "q": query, 
            "start": 1
        }).json()
        search_time = response["searchInformation"]["searchTime"]
        search_results = {}

        for result in response["items"]:
            if (
                "author" in result["pagemap"]["metatags"][0]
                and "article:published_time" in result["pagemap"]["metatags"][0]
            ):
                search_results[result["title"]] = {
                    "url": self.format_url(result["link"]),
                    "author": result["pagemap"]["metatags"][0]["author"],
                    "date": result["pagemap"]["metatags"][0][
                        "article:published_time"
                    ].split("T")[0],
                }
            elif "author" in result["pagemap"]["metatags"][0]:
                search_results[result["title"]] = {
                    "url": self.format_url(result["link"]),
                    "author": result["pagemap"]["metatags"][0]["author"],
                    "date": "Unknown",
                }
            elif "article:published_time" in result["pagemap"]["metatags"][0]:
                search_results[result["title"]] = {
                    "url": self.format_url(result["link"]),
                    "author": "Unknown",
                    "date": result["pagemap"]["metatags"][0][
                        "article:published_time"
                    ].split("T")[0],
                }
            else:
                search_results[result["title"]] = {
                    "url": self.format_url(result["link"]),
                    "author": "Unknown",
                    "date": "Unknown",
                }
        return search_results, search_time


    def format_url(self, url: str) -> str:
        """
        Formats the url to remove the trailing slash.
        """
        char = "/.../"
        if char in url:
            split = url.split(char)
            return split[0] + "/" + split[1]
        return url


if __name__ == "__main__":
    API_KEY = os.environ.get("GOOGLE_API_KEY")
    CX = os.environ.get("CX")
    URL = "https://www.googleapis.com/customsearch/v1"

    search = Search(API_KEY, CX, URL)
    custom_search = search.custom_search("Braised Short Ribs")
    print(custom_search)
