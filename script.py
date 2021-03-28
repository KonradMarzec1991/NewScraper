from collections import namedtuple
import requests
from bs4 import BeautifulSoup

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
            depth_1=('section', {'id', 'special'}),
            depth_2='img'
        ),
        urlNews(
            origin='polsatnews',
            url=generate_url('polsatnews'),
            depth_1=('div', {'id': 'sg_slider'}),
            depth_2='img'
        )
    )

    def get_onet(self):
        soup = create_soup('https://www.onet.pl/')
        my_divs = soup.find_all('div', {'class': 'hpLiveColumn'})

        one = my_divs[0]
        headers = one.find_all('span', {'class': 'title'})
        # return list(h.text for h in headers)

        for h in headers:
            new = News(
                origin='onet',
                header=h.text
            )
            new.save()
        return 'SUCCESS!'

    def get_wp(self):
        soup = create_soup('https://www.onet.pl/')
        my_divs = soup.find_all('div', {'class', 'sc-1010b23-0 jmZodu'})

        one = my_divs[0]
        headers = one.find_all('div', {'class': 'sc-1k2mbc5-1'})
        return list(h.text for h in headers)

    def get_interia(self):
        soup = create_soup('https://www.onet.pl/')
        my_divs = soup.find_all('section', {'id', 'special'})

        print(my_divs)

        one = my_divs[0]
        headers = one.find_all('img')
        return list(h.text for h in headers)


def get_polsat():
    soup = create_soup('https://www.polsatnews.pl/')
    my_divs = soup.find_all('div', {'id': 'sg_slider'})

    one = my_divs[0]

    headers = one.find_all('img')
    print(headers)
    return list(h['alt'] for h in headers)


print(get_polsat())