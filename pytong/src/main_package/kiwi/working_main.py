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
driver = webdriver.Firefox(options=firefox_options)

# Open the web page
driver.get(url)

# Wait for the page to load completely
#wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10) # seconds

result_list = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div") 
results = result_list[1].find_elements(By.CSS_SELECTOR, '[class*=ResultCardcommonstyled]')

for result in results:
    print(result.text)