import requests
import os

API_KEY = os.environ.get("GOOGLE_API_KEY")
CX = os.environ.get("CX")
URL = "https://www.googleapis.com/customsearch/v1"


def custom_search(query: str, start: int) -> dict:
    """
    Custom search function using the custom search API.
    """
    inputs = {"key": API_KEY, "cx": CX, "q": query, "start": start}
    response = requests.get(URL, params=inputs).json()
    search_time = response["searchInformation"]["searchTime"]
    search_results = {}

    for result in response["items"]:
        if (
            "author" in result["pagemap"]["metatags"][0]
            and "article:published_time" in result["pagemap"]["metatags"][0]
        ):
            search_results[result["title"]] = {
                "url": format_url(result["link"]),
                "author": result["pagemap"]["metatags"][0]["author"],
                "date": result["pagemap"]["metatags"][0][
                    "article:published_time"
                ].split("T")[0],
            }
        elif "author" in result["pagemap"]["metatags"][0]:
            search_results[result["title"]] = {
                "url": format_url(result["link"]),
                "author": result["pagemap"]["metatags"][0]["author"],
                "date": "Unknown",
            }
        elif "article:published_time" in result["pagemap"]["metatags"][0]:
            search_results[result["title"]] = {
                "url": format_url(result["link"]),
                "author": "Unknown",
                "date": result["pagemap"]["metatags"][0][
                    "article:published_time"
                ].split("T")[0],
            }
        else:
            search_results[result["title"]] = {
                "url": format_url(result["link"]),
                "author": "Unknown",
                "date": "Unknown",
            }
    return search_results, search_time


def format_url(url: str) -> str:
    """
    Formats the url to remove the trailing slash.
    """
    char = "/.../"
    if char in url:
        split = url.split(char)
        return split[0] + "/" + split[1]
    return url


if __name__ == "__main__":
    # My favourite dish to cook!
    print(custom_search("Braised Short Ribs", 1))
    # print(
    #     format_url(
    #         "https://www.foodnetwork.com/recipes/.../braised-short-ribs-recipe0-1943261"
    #     )
    # )
