from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import utils

class UniversalScraper:
    def __init__(self, url):
        self.url = url
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def scrape_website(self):
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return self.parse_website(soup)

    def parse_website(self, soup):
        website_data = {}
        cards = soup.find_all()
        for card in cards:
            question = card.text
            website_data[question] = ''
        return website_data

    def close(self):
        self.driver.quit()

def scrape_website(url):
    scraper = UniversalScraper(url)
    try:
        website_data = scraper.scrape_website()
        utils.save_data(website_data)
    except Exception as e:
        print(f'Error occurred: {e}')
    finally:
        scraper.close()