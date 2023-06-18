import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from time import time
from utils.utils import parse_offer
    
# URL of the page to scrape
url = 'https://www.skyscanner.pl/transport/loty/waw/tlv/230707/230715/?adultsv2=2&cabinclass=economy&childrenv2=&inboundaltsenabled=false&is_banana_refferal=true&outboundaltsenabled=false&preferdirects=false&qp_prevScreen=HOMEPAGE&ref=home&rtn=1'

# Set up firefox options
firefox_options = Options()
#firefox_options.add_argument('--headless')  # Run firefox in headless mode

# Launch the firefox browser
driver = webdriver.Firefox(options=firefox_options)

# Open the web page
driver.get(url)

# wait for third offer to be able to be selected

driver.implicitly_wait(10)
#element = WebDriverWait(driver, 15).until(
#EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[3]/a/div/div[2]/div/button")))
#driver.execute_script("arguments[0].click();", element)

elements = driver.find_elements(By.XPATH, "//*[@class='FlightsTicket_container']")

offer_list = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]") 
offer_objects = offer_list[0].find_elements(By.XPATH, "./child::*")
offers = [result.text for result in offer_objects]

legit_results = [result for result in offers if "ResultCardcommonstyled" in Selector(text=result.get_attribute("class"))._text]

#for result in legit_results:
#    parse_offer(result)
