import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from time import time
from utils.utils import parse_offer
    
# URL of the page to scrape
url = 'https://www.kiwi.com/en/search/results/copenhagen-denmark/tel-aviv-israel/2024-03-07/2024-03-15?sortBy=price&sortAggregateBy=price&adults=2&children=0&infants=0&bags=0.1_0.0-'

# Set up firefox options
firefox_options = Options()
firefox_options.add_argument('--headless')  # Run firefox in headless mode

# Launch the firefox browser
#driver = webdriver.Firefox(options=firefox_options)
driver = webdriver.Firefox(options=firefox_options)

# Open the web page
driver.get(url)
last_height = driver.execute_script('return document.body.clientHeight') 
driver.execute_script('window.scrollTo(0, document.body.clientHeight);') 

# wait for third offer to be able to be selected
element = WebDriverWait(driver, 15).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div[2]/div[2]/div/span/a")))
#EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/span/a")))

#/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div[2]/div[2]/div/span/a
second = element.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]")

#element2 = WebDriverWait(driver, 15).until(
#EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div[2]/div[2]/div/span/a")))

fourth = element.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[5]")

result_list = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div") 
#results = result_list[0].find_elements(By.CSS_SELECTOR, '[class*=ResultCardcommonstyled]')
results1 = result_list[0].find_elements(By.XPATH, "./child::*")
results = [result.text for result in results1]

legit_results = [result for result in results1 if "ResultCardcommonstyled" in Selector(text=result.get_attribute("class"))._text]

for result in results:
    parse_offer(result)

# example output: '23:10\nWarsaw Chopin\nWAW\n20h 20m\n1 stop\n20:30\n+1\nBen Gurion\nTLV\nFri 8 Mar\n7 nights in Tel Aviv\n11:40\nBen Gurion\nTLV\n4h 10m\nDirect\n14:50\nWarsaw Chopin\nWAW\nSelf-transfer hack\n20 kg\n2,593 zł\nSelect'
# Thu 7 Mar\n14:10Warsaw\nWarsaw Chopin\n(WAW)\n3h 45m\nDirect\n18:55Tel Aviv\nBen Gurion\n(TLV)\n8 nights in Tel Aviv\nFri 15 Mar\n11:40Tel Aviv\nBen Gurion\n(TLV)\n4h 10m\nDirect\n14:50Warsaw\nWarsaw Chopin\n(WAW)\nEconomy\n20 kg\n2,768 zł\nSelect
# 