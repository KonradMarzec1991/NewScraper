"""
Module contains portal-designed classes for scraping main board news
"""

import abc
from typing import List

from bs4.element import Tag

from .utils import create_soup
from .models import News


class Service(abc.ABC):
    """Helper class for main services"""

    @abc.abstractmethod
    def get_board(self):
        """Save list of news from top board"""
        pass

    def save_news(self, obj_list: List[Tag]) -> None:
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

    def get_self_name(self) -> str:
        return self.__class__.__name__.lower()


class Onet(Service):
    """Onet dedicated service"""

    soup = create_soup('onet')
    labels = ('news', 'sport', 'economy')

    def get_board(self) -> None:
        hs = self.soup.find_all(
            name='div',
            attrs={'class': 'hpLiveColumn'}
        )
        for h in hs:
            headers = h.find_all(
                name='span',
                attrs={'class': 'title'}
            )
            self.save_news(headers)

    def get_news(self) -> None:
        hs = self.soup.find_all(
            name='article',
            attrs={'class': 'newsBox'}
        )
        for item in hs:
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
        hs = self.soup.find_all(
            name='div',
            attrs={'id': 'sg_slider'}
        )
        headers = hs[0].find_all('img')
        self.save_news(headers)

    def get_news(self) -> None:
        hs = self.soup.find_all(
            name='ul',
            attrs={'id': 'najnowsze'}
        )
        headers = hs[0].find_all('h2')
        self.save_news(headers)


class Interia(Service):
    """Interia dedicated service"""

    soup = create_soup('interia')
    labels = ('facts', 'business', 'sport')

    def get_board(self) -> None:
        for label in self.labels:
            hs = self.soup.find_all(
                name='section',
                attrs={'id': label}
            )
            headers = hs[0].find_all('a')
            self.save_news(headers)


class Wp(Service):
    """Wp dedicated service"""

    soup = create_soup('wp')

    def get_board(self) -> None:
        hs = self.soup.find_all(
            name='div',
            attrs={'class': 'sc-1010b23-0 crydSY'}
        )

        headers = hs[0].find_all(
            name='div',
            attrs={'class': 'sc-1qdlbrk-0'}
        )
        self.save_news(headers)
