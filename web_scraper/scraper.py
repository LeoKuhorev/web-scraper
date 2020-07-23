import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Uladzimir_Nyaklyayew'
URL = 'https://en.wikipedia.org/wiki/Washington_(state)'


def get_soup(URL):
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    return soup


def get_citations_list(soup):
    content = soup.find('div', id='content')
    citations = content.find_all('a', title='Wikipedia:Citation needed')
    citations_text = [c.parent.parent.parent.text.replace(
        '[citation needed]', '') for c in citations]

    return citations_text


def get_citations_needed_count(URL):
    soup = get_soup(URL)
    citations = get_citations_list(soup)

    return len(citations)


def get_citations_needed_report(URL):
    soup = get_soup(URL)
    citations = get_citations_list(soup)
    output = ''
    for c in citations:
        output += f'Citation needed for {c} \n'

    return output


if __name__ == "__main__":
    length = get_citations_needed_count(URL)
    string = get_citations_needed_report(URL)

    print(f'Number of citations needed {length}')
    print(string)