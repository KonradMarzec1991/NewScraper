import requests
from bs4 import BeautifulSoup


def get_webpage_html(url):
    response = requests.get(url)
    return response.content


soup = BeautifulSoup(get_webpage_html('https://www.onet.pl/'))
mydivs = soup.find_all('div', {'class': 'hpLiveColumn'})

one = mydivs[0]
headears = one.find_all('span', {'class': 'title'})

for h in headears:
    print(h.text)
