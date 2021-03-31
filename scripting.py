from news.utils import create_soup


class Wp:
    soup = create_soup('wp')

    def get_board(self):
        hs = self.soup.find_all(
            name='div',
            attrs={'class': 'sc-1010b23-0 jmZodu'}
        )
        headers = hs[0].find_all('div', {'class': 'sc-1qdlbrk-0 drKsxm sc-1k2mbc5-1'})
        print(list(h.text for h in headers))

    def get_news(self):
            b = self.soup.find_all('div', {'class': 'msqvd4-0'})
            for item in b:
                print(item)


print(Wp().get_news())

