import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # supplies driver as argument
from selenium.webdriver.support import expected_conditions as EC

import time
import random
from datetime import datetime

DRIVER_PATH = '/Users/max/Desktop/chromedriver/chromedriver'
service = Service(DRIVER_PATH) # need to create service object using path
driver = webdriver.Chrome(service=service)
driver.get('https://student.iclicker.com/')


wait = WebDriverWait(driver, 30) # catch exception
join_wait = WebDriverWait(driver, 30)

input("Please login")

join_button = join_wait.until(EC.element_to_be_clickable((By.ID, "btnJoin")))
join_button.click()

START_TIME = datetime.now()

while True:
    print("hi")
    time.sleep(5)
    current_time = datetime.now()
    if ( 3 < (current_time.hour - START_TIME.hour)):
        driver.quit()
        exit()
        break

    selectedButton = driver.find_element(By.CLASS_NAME, "btn-selected")
    if (not selectedButton):
        button_b = wait.until(EC.presence_of_element_located(By.ID, "multiple-choice-b"))
        time.sleep(random.randint(10,20))
        button_b.click()