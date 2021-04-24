import requests
from bs4 import BeautifulSoup


def create_soup(service_name):
    response = requests.get(
        url=f'https://www.{service_name}.pl',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return BeautifulSoup(response.content, "html.parser")


soup = create_soup('polsatnews')


def get_board(soup):
    hs = soup.find_all(
        name='div',
        attrs={'id': 'sg_slider'}
    )
    headers = hs[0].find_all('img')
    print(list(type(h) for h in headers))


print(get_board(soup))