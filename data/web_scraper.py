from typing import List
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

blacklist = [
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

unecessary_words = [
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
]


def get_website_text(
    url: str,
    blacklist: List[str] = blacklist,
    unecessary_words: List[str] = unecessary_words,
) -> List[str]:
    """
    Returns a list of all the text on a website filtered to eliminate blacklisted and unecessary words.
    """
    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }
    req = Request(url, headers=hdr)
    website = urlopen(req)
    soup = BeautifulSoup(website, "html.parser")
    website_text = soup.findAll(text=True)
    output = ""
    list_output = []

    for t in website_text:
        if (
            t.parent.name not in blacklist
            and len(t) > 1
            and not any(word in t.lower() for word in unecessary_words)
        ):
            output += "{} ".format(t)
            list_output.append(t)

    return output


if __name__ == "__main__":
    # Interesting lecture I read recently
    print(
        get_website_text(
            "https://www.bloomberg.com/news/articles/2022-08-16/biden-signs-tax-climate-bill-marking-long-sought-democratic-win?srnd=politics-vp"
        )
    )
