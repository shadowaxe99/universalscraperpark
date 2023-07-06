# Universal Scraper

This repository contains a Python program that scrapes data from any website, despite normal scrapers not working. 

## Installation

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Import the `UniversalScraper` class from `scraper.py` and the `utils` module from `utils.py` in your `main.py` file.
2. Define the Website URL you want to scrape as `Website_URL`.
3. Create an instance of `UniversalScraper` and call the `scrape_website` function with `Website_URL` as the argument.

Here is a sample usage:

```python
from scraper import UniversalScraper
import utils

Website_URL = 'https://example.com/'

scraper = UniversalScraper()
scraper.scrape_website(Website_URL)
```

## Dependencies

This program uses the following Python libraries:

- requests
- BeautifulSoup
- selenium
- webdriver_manager

These dependencies are listed in the `requirements.txt` file.

## Contributing

Please read through our contributing guidelines. Included are directions for opening issues, coding standards, and notes on development.

## License

This project is licensed under the MIT License.