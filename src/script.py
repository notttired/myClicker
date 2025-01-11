
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = '/Users/max/Desktop/chromedriver/chromedriver'
service = Service(DRIVER_PATH) # need to create service object using path
driver = webdriver.Chrome(service=service)

# take in  list of things to search for, limit 50 items
# enter location: searches close by prices

class information:
    def __init__(location, query, limit):
        self.location = location
        self.query = query
        self.limit = limit

class websites:
    def __init__(siteURL, search_XPATH, price_XPATH, weight_XPATH, info_XPATH, unit_price_XPATH):
        self.siteURL = siteURL
        self.search_XPATH = search_XPATH
        self.price_XPATH = price_XPATH
        self.weight_XPATH = weight_XPATH
        self.info_XPATH = info_XPATH
        self.unit_price_XPATH

    

# data-automation-id, data-automation-price

search_bar = driver.findElement(By.XPATH, "...")

# Navigate to the URL
driver.get('https://walmart.com')

print(driver.page_source)
# It's a good practice to close the browser when done
driver.quit()