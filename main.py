import requests
from scraper import UniversalScraper, scrape_website
import utils

Website_URL = ''

def main():
    scraper = UniversalScraper(requests)
    print('Scraping started')
    try:
        scrape_website(scraper, Website_URL)
        print('Scraping completed')
    except Exception as e:
        print('Error occurred: ', e)
        utils.log_error(e)

if __name__ == '__main__':
    main()