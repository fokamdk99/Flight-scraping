import requests
from bs4 import BeautifulSoup

# Path to your chromedriver executable
webdriver_path = '/path/to/chromedriver'

# URL of the page to scrape
url = 'https://www.kiwi.com/en/search/results/warsaw-poland/male-maldives/2024-02-04/2024-02-14?sortBy=price&sortAggregateBy=price&adults=2&children=0&infants=0&bags=0.1_0.0-'


# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements with class names containing 'item-'
elements = soup.find_all(class_=lambda value: value and 'ResultListstyled' in value)

# Print the extracted elements
for element in elements:
    new_element = soup.select_one('[data-test="ResultList-results"]')
    print(new_element)