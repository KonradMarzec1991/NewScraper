from collections import namedtuple

import requests
from bs4 import BeautifulSoup

from .models import News


urlNews = namedtuple('urlNews', 'origin url depth_1 depth_2')


def generate_url(name):
    return f'https://www.{name}.pl'


def create_soup(url):
    response = requests.get(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return BeautifulSoup(response.content, "html.parser")


class Scraper:

    url_list = (
        urlNews(
            origin='onet',
            url=generate_url('onet'),
            depth_1=('div', {'class': 'hpLiveColumn'}),
            depth_2=('span', {'class': 'title'})
        ),
        urlNews(
            origin='wp',
            url=generate_url('wp'),
            depth_1=('div', {'class', 'sc-1010b23-0 jmZodu'}),
            depth_2=('div', {'class': 'sc-1k2mbc5-1'})
        ),
        urlNews(
            origin='interia',
            url=generate_url('interia'),
            depth_1=('section', {'id', 'facts'}),
            depth_2='a'
        ),
        urlNews(
            origin='polsatnews',
            url=generate_url('polsatnews'),
            depth_1=('div', {'id': 'sg_slider'}),
            depth_2='img'
        )
    )

    def get_news(self):
        for data in self.url_list:
            origin, url, depth_1, depth_2 = data
            frame = create_soup(url).find_all(*depth_1)[0]

            if isinstance(depth_2, tuple):
                headers = frame.find_all(*depth_2)
            else:
                headers = frame.find_all(depth_2)

            for header in headers:
                new = News(
                    origin=origin,
                    header=header.text.strip()
                    if origin != 'polsatnews' else header['alt']
                )
                new.save()


class Onet:
    def __init__(self):
        self.soup = create_soup(generate_url('onet'))

    def get_board(self):
        hs = self.soup.find_all('div', {'class': 'hpLiveColumn'})[0]
        headers = hs.find_all('span', {'class': 'title'})
        print(list(h.text for h in headers))

    def get_news(self):
        hs = self.soup.find_all('article', {'class': 'newsBox'})
        for item in hs:
            try:
                if item.section['data-section'] in ('news', 'sport', 'economy'):
                    headers = item.find_all('span', {'class': 'title'})
                    print(list(h.text.strip() for h in headers))
            except TypeError:
                pass


class Polsanews:
    def __init__(self):
        self.soup = create_soup(generate_url('polsatnews'))

    def get_board(self):
        hs = self.soup.find_all('div', {'id': 'sg_slider'})[0]
        headers = hs.find_all('img')
        print(list(h['alt'] for h in headers))

    def get_news(self):
        hs = self.soup.find_all('ul', {'id': 'najnowsze'})
        headers = hs[0].find_all('h2')
        print(list(h.text for h in headers))
