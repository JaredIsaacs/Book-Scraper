from urllib.request import Request, urlopen
from html_parser import Parser

class Scraper():
    def __init__(self):
        self.html_parser = Parser()

    def get_page(self, url: str) -> str:
        req = Request(url, headers={'User-Agent': 'Magic Browser'})

        page = urlopen(req)
        html = page.read().decode('utf-8')

        return html

    def get_page_numbers(self, url: str) -> int:
        page = self.get_page(url)
        pagination = self.html_parser.get_class('digg_pagination', page)

        if pagination == '':
            return 0

        a_elements = self.html_parser.get_elements('a', pagination)
        page_number = self.html_parser.get_number(a_elements[len(a_elements) - 2])


        return page_number


scraper = Scraper()
print(scraper.get_page_numbers('https://www.novelupdates.com/series/a-sweet-girl-wont-be-fooled-by-the-villainess/'))