import unittest
import html_parser
import scrape


class TestScraper(unittest.TestCase):
    def setUp(self):
        self.parser = html_parser.Parser()
        self.scraper = scrape.Scraper()
        

    def test_get_page_numbers(self):
        self.assertEqual(self.scraper.get_page_numbers(
            'https://www.novelupdates.com/series/the-grand-secretarys-pampered-wife/'), 60)


    def test_get_page_number_zero(self):
        self.assertEqual(self.scraper.get_page_numbers(
            'https://www.novelupdates.com/series/i-only-want-you/'), 0)
        


    def test_get_latest_chapter_quad(self):
        self.assertEqual(self.scraper.get_latest_chapter(
            'https://www.novelupdates.com/series/heroes-of-marvel/'), 1164)


    def test_get_latest_chapter_triple(self):
        self.assertEqual(self.scraper.get_latest_chapter(
            'https://www.novelupdates.com/series/the-grand-secretarys-pampered-wife/'), 515)
        
    

    def test_get_latest_chapter_double(self):
        self.assertEqual(self.scraper.get_latest_chapter(
            'https://www.novelupdates.com/series/naruto-sakura-blizzard/'), 84)
        

    def test_get_latest_chapter_single(self):
        self.assertEqual(self.scraper.get_latest_chapter(
            'https://www.novelupdates.com/series/i-only-want-you/'), 8)


    def test_get_latest_chapter_vschema(self):
        self.assertEqual(self.scraper.get_latest_chapter(
            'https://www.novelupdates.com/series/an-unexpected-exile-and-the-slow-life-that-followed/'), 79)
        

if __name__ == '__main__':
    unittest.main()