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
url = 'https://www.azair.eu/azfin.php?tp=0&searchtype=flexi&srcAirport=Vienna+%5BVIE%5D&srcTypedText=vien&srcFreeTypedText=&srcMC=&srcFreeAirport=&dstAirport=Poland+%5BSZY%5D+%28%2BWMI%2CWAW%2CGDN%2CBZG%2CLCJ%2CLUZ%2CPOZ%2CKRK%2CKTW%2CRZE%2CSZZ%2CWRO%29&dstTypedText=pola&dstFreeTypedText=&dstMC=PL&adults=2&children=0&infants=0&minHourStay=0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00&maxHourOutbound=24%3A00&minHourInbound=0%3A00&maxHourInbound=24%3A00&dstap0=WMI&dstap1=WAW&dstap2=GDN&dstap3=BZG&dstap4=LCJ&dstap6=LUZ&dstap8=POZ&dstap10=KRK&dstap11=KTW&dstap12=RZE&dstap13=SZZ&dstap14=WRO&dstFreeAirport=&depdate=27.7.2023&arrdate=27.7.2023&minDaysStay=5&maxDaysStay=5&nextday=0&autoprice=true&currency=EUR&wizzxclub=false&flyoneclub=false&blueairbenefits=false&megavolotea=false&schengen=false&transfer=true&samedep=true&samearr=true&dep0=true&dep1=true&dep2=true&dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&maxChng=1&isOneway=oneway&resultSubmit=Search'

# Set up firefox options
firefox_options = Options()
firefox_options.add_argument('--headless')  # Run firefox in headless mode

# Launch the firefox browser
driver = webdriver.Firefox(options=firefox_options)

# Open the web page
driver.get(url)

# wait for third offer to be able to be selected
driver.implicitly_wait(10)

offer_list = driver.find_elements(By.ID, "reslist") 
offer_objects = offer_list[0].find_elements(By.XPATH, "./child::*")
offers = [result.text for result in offer_objects]

legit_results = [result for result in offers if "ResultCardcommonstyled" in Selector(text=result.get_attribute("class"))._text]

for result in legit_results:
    parse_offer(result)
