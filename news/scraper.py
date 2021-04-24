from news.utils import create_soup


class Service:
    pass


class OnetService:
    soup = create_soup('onet')
    labels = ('news', 'sport', 'economy')

    def get_board(self):
        hs = self.soup.find_all(
            name='div',
            attrs={'class': 'hpLiveColumn'}
        )
        for h in hs:
            headers = h.find_all(
                name='span',
                attrs={'class': 'title'}
            )
            print(list(h.text.strip() for h in headers))

    def get_news(self):
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
                    print(list(h.text.strip() for h in headers))
            except TypeError:
                pass


class PolsatnewsService:
    soup = create_soup('onet')

    def get_board(self):
        hs = self.soup.find_all(
            name='div',
            attrs={'id': 'sg_slider'}
        )
        headers = hs[0].find_all('img')
        print(list(h['alt'] for h in headers))

    def get_news(self):
        hs = self.soup.find_all(
            name='ul',
            attrs={'id': 'najnowsze'}
        )
        headers = hs[0].find_all('h2')
        print(list(h.text for h in headers))


class InteriaService:
    soup = create_soup('interia')
    labels = ('facts', 'business', 'sport')

    def get_news(self):
        for label in self.labels:
            hs = self.soup.find_all(
                name='section',
                attrs={'id': label}
            )
            headers = hs[0].find_all('a')
            print(list(h.text for h in headers))


class Wp:
    soup = create_soup('wp')

    def get_board(self):
        hs = self.soup.find_all(
            name='div',
            attrs={'class': 'sc-1010b23-0 crydSY'}
        )
        print(hs)

        headers = hs[0].find_all(
            name='div',
            attrs={'class': 'sc-1qdlbrk-0'}
        )

        print(list(h.text for h in headers))