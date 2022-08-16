from typing import Tuple

# Currently only supports MLA and APA citations.

def apa_citation(author: str, title: str, year: str, publisher: str, edition: str = '1st', url: str = '') -> Tuple[str, str]:
    """
    Generates an APA citation.
    Format:
    Author’s Last Name, First Initial. (Year). Title 
    (Edition ed.). Publisher.
    """
    last_name = author.split(' ')[-1]
    first_initial = author.split(' ')[0][0]
    full = f'{last_name.capitalize()}, {first_initial}. ({year}). {title} \n ({edition} ed.). {publisher}.'
    text = f'({last_name}, {year})'

    if url != '':
        full += '\n' + url
    return full, text

def mla_citation(author, title: str, year: str, publisher: str, edition: str = '1st', url: str = '') -> Tuple[str, str]:
    """
    Generates an MLA citation.
    Format:
    Author’s Last Name, First Name. Title of Book. Edition, Publisher, 
    Year of publication.
    """
    last_name = author.split(' ')[-1]
    first_name = author.split(' ')[0]
    full = f'{last_name.capitalize()}, {first_name.capitalize()}. {title}. {edition}, {publisher}, \n{year}.'
    text = f'({last_name}, {year})'

    if url != '':
        full += ' ' + url
    return full, text

if __name__ == '__main__':
    pass