import requests
from bs4 import BeautifulSoup


def get_soup(URL: str) -> object:
    """Get the content of the entire Wikipedia page

    Args:
        URL (str): URL of the Wikipedia page to be captured

    Returns:
        obj: BeautifulSoup object
    """
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    return soup


def get_citations_list(soup: object) -> list:
    """Get a list of the citations from the passed in wikipedia page

    Args:
        soup (obj): BeautifulSoup object

    Returns:
        list: List of citation texts
    """
    content = soup.find('div', id='content')
    citations = content.find_all('a', title='Wikipedia:Citation needed')
    citations_text = [c.parent.parent.parent.text.strip().replace(
        '[citation needed]', '') for c in citations]

    return citations_text


def get_citations_needed_count(URL: str) -> int:
    """Get the count of citations from the passed in Wikipedia page URL

    Args:
        URL (str): URL of the Wikipedia page

    Returns:
        int: Number of citations on the page
    """
    soup = get_soup(URL)
    citations = get_citations_list(soup)

    return len(citations)


def get_citations_needed_report(URL: str) -> str:
    """Get the report of the passages that need a citation to be added

    Args:
        URL (str): URL of the Wikipedia page

    Returns:
        str: Citation report
    """
    soup = get_soup(URL)
    citations = get_citations_list(soup)
    output = ''
    for c in citations:
        output += f'Citation needed for {c} \n'

    return output
