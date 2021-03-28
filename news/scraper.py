import requests
from bs4 import BeautifulSoup

from .models import News


def get_webpage_html(url):
    response = requests.get(url)
    return response.content


# for onet
def get_onet():
    soup = BeautifulSoup(
        get_webpage_html('https://www.onet.pl/'),
        "html.parser"
    )
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


# for wp
def get_wp():
    soup = BeautifulSoup(
        get_webpage_html('https://www.wp.pl/'),
        "html.parser"
    )
    my_divs = soup.find_all('div', {'class', 'sc-1010b23-0 jmZodu'})

    one = my_divs[0]
    headers = one.find_all('div', {'class': 'sc-1k2mbc5-1'})
    return list(h.text for h in headers)


# for interia
def get_interia():
    soup = BeautifulSoup(
        get_webpage_html('https://www.interia.pl/'),
        "html.parser"
    )
    my_divs = soup.find_all('section', {'id', 'special'})

    one = my_divs[0]
    headers = one.find_all('img')
    return list(h.text for h in headers)


# for polsat news
def get_polsat():
    r = requests.get(
        'https://www.polsatnews.pl',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    soup = BeautifulSoup(
        r.content,
        "html.parser"
    )
    my_divs = soup.find_all('div', {'id': 'sg_slider'})

    one = my_divs[0]
    headers = one.find_all('img')
    return list(h.text for h in headers)
