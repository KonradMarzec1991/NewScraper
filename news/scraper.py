from .utils import create_soup


class OnetService:
    soup = create_soup('onet')

    def get_board(self):
        hs = self.soup.find_all('div', {'class': 'hpLiveColumn'})
        headers = hs[0].find_all('span', {'class': 'title'})
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


class PolsanewsService:
    soup = create_soup('onet')

    def get_board(self):
        hs = self.soup.find_all('div', {'id': 'sg_slider'})[0]
        headers = hs.find_all('img')
        print(list(h['alt'] for h in headers))

    def get_news(self):
        hs = self.soup.find_all('ul', {'id': 'najnowsze'})
        headers = hs[0].find_all('h2')
        print(list(h.text for h in headers))


class InteriaService:
    soup = create_soup('interia')
    labels = ('facts', 'business', 'sport')

    def get_news(self):
        for label in self.labels:
            hs = self.soup.find_all('section', {'id', label})[0]
            headers = hs.find_all('a')
            print(list(h.text for h in headers))
