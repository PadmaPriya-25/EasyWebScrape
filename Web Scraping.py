import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_data(soup, tag, attribute):
    data = []
    for element in soup.find_all(tag, attribute):
        data.append(element.text.strip())
    return data

def present_data(data):
    print("Scraped Data:")
    for item in data:
        print(item)
def main():
    url = input("Enter website URL: ")
    tag = input("Enter HTML tag to scrape (e.g., h1, p, li): ")
    attribute = input("Enter attribute to filter by (e.g., class, id): ")
    
    soup = scrape_website(url)
    data = extract_data(soup, tag, attribute)
    present_data(data)

if __name__ == "__main__":
    main()  