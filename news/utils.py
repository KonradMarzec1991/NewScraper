"""
This module contains helper function for scraper and/or model
"""

from abc import ABCMeta

import requests
from bs4 import BeautifulSoup


def create_soup(service_name):
    """This function creates bs4 object for given news service"""
    response = requests.get(
        url=f'https://www.{service_name}.pl',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return BeautifulSoup(response.content, "html.parser")


class MetaSingleton(ABCMeta):
    """This class introduces Singleton pattern"""
    instances = {}

    def __call__(cls, *args, **kwargs):
        existing_instance = MetaSingleton.instances.get(cls, None)
        if existing_instance is None:
            MetaSingleton.instances[cls] = super().__call__(*args, **kwargs)
        return MetaSingleton.instances[cls]


class Singleton(metaclass=MetaSingleton):
    """Class ready for inheritance"""
    pass
