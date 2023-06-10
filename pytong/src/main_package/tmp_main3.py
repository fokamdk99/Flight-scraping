from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the page to scrape
url = 'https://www.kiwi.com/en/search/results/warsaw-poland/male-maldives/2024-02-04/2024-02-14?sortBy=price&sortAggregateBy=price&adults=2&children=0&infants=0&bags=0.1_0.0-'

# Set up firefox options
firefox_options = Options()
firefox_options.add_argument('--headless')  # Run firefox in headless mode
firefox_options.add_argument("window-size=1980,1030")

# Launch the firefox browser
#driver = webdriver.Firefox(options=firefox_options)
driver = webdriver.Firefox(options=firefox_options)

# Open the web page
driver.get(url)

# Wait for the page to load completely
#wait = WebDriverWait(driver, 10)
#driver.implicitly_wait(10) # seconds
element = WebDriverWait(driver, 15).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/span/a")))

items = [] 
 
# instantiate height of webpage 
last_height = driver.execute_script('return document.body.clientHeight') 
 
# set target count 
itemTargetCount = 5 
 
# scroll to bottom of webpage 
while itemTargetCount > len(items): 
	driver.execute_script('window.scrollTo(0, document.body.clientHeight);') 
 
	# wait for content to load 
	time.sleep(5) 
 
	new_height = driver.execute_script('return document.body.clientHeight') 
 
	if new_height == last_height: 
		break 
 
	last_height == new_height 
	
	result_list = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div/div")
	results = result_list[0].find_elements(By.CSS_SELECTOR, '[class*=ResultCardcommonstyled]')
	h4_texts = [element.text for element in results] 
 
	items.extend(h4_texts) 
 
	# print title 
	print(h4_texts)


for item in items:
	print(item)