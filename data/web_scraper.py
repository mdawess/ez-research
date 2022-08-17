import re
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
    "code of conduct",
    "accessibility policy",
]


def get_website_text(
    url: str,
    blacklist: List[str] = blacklist,
    unecessary_words: List[str] = unecessary_words,
) -> str:
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

    return format_output(output)

def format_output(output: str) -> str:
    """
    Formats the output to remove extra spaces and newlines
    so the ai can read the text better. Then adds a newline
    with TLDR to incite the summary generation.
    """
    formatted_output = re.sub('\s+',' ', output)
    return formatted_output + "\n\nTLDR:"


if __name__ == "__main__":
    # Interesting lecture I read recently
    print(
        get_website_text(
            "http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html?curius=1466"
        )
    )
