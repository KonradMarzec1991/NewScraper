import requests
from bs4 import BeautifulSoup


def create_soup(service_name):
    response = requests.get(
        url=f'https://www.{service_name}.pl',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return BeautifulSoup(response.content, "html.parser")
