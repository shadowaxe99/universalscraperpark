from bs4 import BeautifulSoup

def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def extract_data(soup, element_id):
    element = soup.find(id=element_id)
    if element:
        return element.text.strip()
    return None

def log_message(message):
    print(message)