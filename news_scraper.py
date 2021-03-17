import requests
from bs4 import BeautifulSoup


def get_webpage_html(url):
    response = requests.get(url)
    return response.content


# for onet
def get_onet():
    soup = BeautifulSoup(get_webpage_html('https://www.onet.pl/'))
    my_divs = soup.find_all('div', {'class': 'hpLiveColumn'})

    one = my_divs[0]
    headers = one.find_all('span', {'class': 'title'})

    for h in headers:
        print(h.text)


# for wp
def get_wp():
    soup = BeautifulSoup(get_webpage_html('https://www.wp.pl/'))
    my_divs = soup.find_all('div', {'class', 'sc-1010b23-0 jmZodu'})

    one = my_divs[0]
    headers = one.find_all('div', {'class': 'sc-1k2mbc5-1'})

    for h in headers:
        print(h.text)


# for interia
def get_interia():
    soup = BeautifulSoup(get_webpage_html('https://www.interia.pl/'))
    my_divs = soup.find_all('section', {'id', 'special'})

    one = my_divs[0]
    headers = one.find_all('img')

    for h in headers:
        print(h['alt'])
