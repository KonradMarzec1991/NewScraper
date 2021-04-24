"""
This module contains helper function for scraper and/or model
"""

import requests
from bs4 import BeautifulSoup


def create_soup(service_name):
    """This function creates bs4 object for given news service"""
    response = requests.get(
        url=f'https://www.{service_name}.pl',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return BeautifulSoup(response.content, "html.parser")
