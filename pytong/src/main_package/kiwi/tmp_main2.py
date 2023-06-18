import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.kiwi.com/en/search/results/warsaw-poland/male-maldives/2024-02-04/2024-02-14?sortBy=price&sortAggregateBy=price&adults=2&children=0&infants=0&bags=0.1_0.0-'

# Set up firefox options
firefox_options = Options()
firefox_options.add_argument('--headless')  # Run firefox in headless mode

# Launch the firefox browser
#driver = webdriver.Firefox(options=firefox_options)
driver = webdriver.Firefox()

# Wait for the page to load completely
#wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10) # seconds

# Open the web page
driver.get(url)

# Get the page source
page_source = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find elements with class names containing 'item-'
result_list_styled = soup.find_all(class_=lambda value: value and 'ResultListstyled' in value)
result_list0 = result_list_styled[0].select_one('[data-test="ResultList-results"]')
result_list = result_list_styled[1].select_one('[data-test="ResultList-results"]')
print(result_list0)
print(result_list)