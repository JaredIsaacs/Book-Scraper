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
    
    def get_chapter_numbers(self, url: str) -> int:
        page = self.get_page(url)
        tbody = self.html_parser.get_elements('tbody', page)
        tr = self.html_parser.get_elements('tr', tbody[1])
        chapter_numbers = self.html_parser.get_chapter(tr[0])
        
        return chapter_numbers


scraper = Scraper()
url = 'https://www.novelupdates.com/series/the-grand-secretarys-pampered-wife/'
print(scraper.get_page_numbers(url))
numbers = scraper.get_chapter_numbers(url)
print(numbers)
#with open('test.html', 'w', encoding='utf-8') as out:
#    out.write(scraper.get_chapter_numbers(url)[0])