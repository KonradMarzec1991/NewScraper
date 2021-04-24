"""
Module contains portal-designed classes for scraping main board news
"""

import abc
from typing import List

from bs4.element import Tag

from .utils import Singleton, create_soup
from .models import News


class Service(Singleton):
    """Helper class for main services"""

    # pylint: disable=unnecessary-pass
    @abc.abstractmethod
    def get_board(self):
        """Save list of news from top board"""
        pass

    def save_news(self, obj_list: List[Tag]) -> str:
        """
        Save objects from list to db
        :param obj_list: list with headers
        :return: None
        """
        for obj in obj_list:
            header = obj.text.strip()
            if not header:
                if 'alt' in obj.__dict__:
                    header = obj.get('alt').strip()
                # other if else
            news = News(
                origin=self.get_self_name(),
                header=header
            )
            news.save()
        return f'Data from service {self.get_self_name()} loaded successfully.'

    def get_self_name(self) -> str:
        """Returns name of self class"""
        return self.__class__.__name__.lower()


class Onet(Service):
    """Onet dedicated service"""

    soup = create_soup('onet')
    labels = ('news', 'sport', 'economy')

    def get_board(self) -> None:
        board = self.soup.find_all(
            name='div',
            attrs={'class': 'hpLiveColumn'}
        )
        for item in board:
            headers = item.find_all(
                name='span',
                attrs={'class': 'title'}
            )
            self.save_news(headers)

    def get_news(self) -> None:
        """Get news"""
        board = self.soup.find_all(
            name='article',
            attrs={'class': 'newsBox'}
        )
        for item in board:
            try:
                if item.section['data-section'] in self.labels:
                    headers = item.find_all(
                        name='span',
                        attrs={'class': 'title'}
                    )
                    self.save_news(headers)
            except TypeError:
                pass


class PolsatNews(Service):
    """PolsatNews dedicated service"""

    soup = create_soup('polsatnews')

    def get_board(self) -> None:
        board = self.soup.find_all(
            name='div',
            attrs={'id': 'sg_slider'}
        )
        headers = board[0].find_all('img')
        self.save_news(headers)

    def get_news(self) -> None:
        """Get news"""
        board = self.soup.find_all(
            name='ul',
            attrs={'id': 'najnowsze'}
        )
        headers = board[0].find_all('h2')
        self.save_news(headers)


class Interia(Service):
    """Interia dedicated service"""

    soup = create_soup('interia')
    labels = ('facts', 'business', 'sport')

    def get_board(self) -> None:
        for label in self.labels:
            board = self.soup.find_all(
                name='section',
                attrs={'id': label}
            )
            headers = board[0].find_all('a')
            self.save_news(headers)


class Wp(Service):
    """Wp dedicated service"""

    soup = create_soup('wp')

    def get_board(self) -> None:
        board = self.soup.find_all(
            name='div',
            attrs={'class': 'sc-1010b23-0 crydSY'}
        )

        headers = board[0].find_all(
            name='div',
            attrs={'class': 'sc-1qdlbrk-0'}
        )
        self.save_news(headers)


# create singleton objects for each media
wp = Wp()
onet = Onet()
interia = Interia()
polsatnews = PolsatNews()
