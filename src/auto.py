from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # supplies driver as argument
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import random
from datetime import datetime

import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

# accessing and printing value

START_TIME = datetime.now()
info = {
    "email": os.getenv("email"),
    "password": os.getenv("password"),
    "course": os.getenv("course"),
}

options = Options()
options.add_argument("--headless=new")
DRIVER_PATH = '/Users/max/Desktop/chromedriver/chromedriver'
service = Service(DRIVER_PATH) # need to create service object using path
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://student.iclicker.com/')

wait = WebDriverWait(driver, 9000)
page_wait = WebDriverWait(driver, 10)

def login():
    email = page_wait.until(EC.element_to_be_clickable((By.ID, "input-email")))
    email.send_keys(info["email"])
    password = page_wait.until(EC.element_to_be_clickable((By.ID, "input-password")))
    password.send_keys(info["password"])

    submit = page_wait.until(EC.element_to_be_clickable((By.ID, "sign-in-button")))
    submit.click()

def select_course():
    course = page_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, info["course"])))
    course.click()

def join():
    join_wait = WebDriverWait(driver, 300)
    join_button = join_wait.until(EC.element_to_be_clickable((By.ID, "btnJoin")))
    join_button.click()



login()
select_course()
join()

while True:
    time.sleep(5)
    current_time = datetime.now()
    if ( 3 < (current_time.hour - START_TIME.hour)):
        driver.quit()
        exit()
        break

    try:
        print("Button already selected")
        selectedButton = driver.find_element(By.CLASS_NAME, "btn-selected")
    except:
        button_b = wait.until(EC.element_to_be_clickable((By.ID, "multiple-choice-b")))
        print("Found button")
        time.sleep(random.randint(10,20))
        print("Selecting")
        button_b.click()