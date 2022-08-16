from typing import List
from bs4 import BeautifulSoup
import urllib

blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
    'title',
    'h1',
    'h2',
    'h3',
    'h4',
    '\n',
    '(',
    ')',
]

unecessaary_words = [
    'about us',
    'contact us',
    'privacy policy',
    'terms of use',
    'copyright',
    'tags',
    'photo',
    'credit',
    'copyright',
    'all rights reserved',
    'posted',
    'bssl'
]

def get_website_text(url: str, blacklist: List[str], unecessaary_words: List[str]) -> List[str]:
    """
    Returns a list of all the text on a website filtered to eliminate blacklisted and unecessary words.
    """
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    website_text = soup.findAll(text = True)
    output = ''
    list_output = []

    for t in website_text:
        if t.parent.name not in blacklist and \
        len(t) > 1 and not any(word in t.lower() for word in unecessaary_words):
            output += '{} '.format(t)
            list_output.append(t)

    return output, list_output

if __name__ == '__main__':
    # Interesting lecture I read recently
    print(get_website_text(
        'http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html', 
        blacklist, 
        unecessaary_words
    ))





