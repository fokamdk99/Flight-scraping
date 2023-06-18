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
from utils.utils import parse_offer_azair, describe_flight
    
# URL of the page to scrape
url = 'https://www.azair.eu/azfin.php?searchtype=flexi&tp=0&isOneway=oneway&srcAirport=Vienna+%5BVIE%5D&srcFreeAirport=&srcTypedText=vien&srcFreeTypedText=&srcMC=&dstAirport=Malaysia+%5BKUL%5D&dstFreeAirport=&dstTypedText=mala&dstFreeTypedText=&dstMC=MY&depmonth=202307&depdate=2023-07-27&aid=0&arrmonth=202308&arrdate=2023-08-31&minDaysStay=5&maxDaysStay=5&dep0=true&dep1=true&dep2=true&dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&samedep=true&samearr=true&minHourStay=0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00&maxHourOutbound=24%3A00&minHourInbound=0%3A00&maxHourInbound=24%3A00&transfer=true&autoprice=true&adults=2&children=0&infants=0&maxChng=3&currency=EUR&lang=en&indexSubmit=Search'

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

for offer in offers:
    flight = parse_offer_azair(offer)
    describe_flight(flight)

# THERE Thu 27/07/23 08:35 Vienna VIE 09:55 Warsaw WMI 1:20 h / no change\n\n€26.12\n 
# THERE Thu 27/07/23 17:00 Vienna VIE 23:30 Gdansk GDN 6:30 h / 1 change\n\n€116.28\n
# THERE Sat 26/08/23 01:10 Vienna VIE 07:50 Bangkok BKK 25:40 h / 2 changes\nBACK Thu 31/08/23 09:00 Bangkok BKK 22:50 Vienna VIE 18:50 h / 2 changes\n\n€1300.97\nLength of stay: 5 days\n