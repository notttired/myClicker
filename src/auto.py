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

current_directory = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = os.path.join(current_directory, 'chromedriver', 'chromedriver')

START_TIME = datetime.now()
START_TIME_HOUR = START_TIME.hour

info = {
    "email": os.getenv("email"),
    "password": os.getenv("password"),
    "course": os.getenv("course"),
}

options = Options()
options.add_argument("--headless=new")
service = Service(DRIVER_PATH) # need to create service object using path
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://student.iclicker.com/')

page_wait = WebDriverWait(driver, 15)

def login():
    email = page_wait.until(EC.element_to_be_clickable((By.ID, "input-email")))
    email.click()
    email.send_keys(info["email"])
    password = page_wait.until(EC.element_to_be_clickable((By.ID, "input-password")))
    password.click()
    password.send_keys(info["password"])

    try:
        cookies = page_wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
        cookies.click()
    except:
        pass
    submit = page_wait.until(EC.element_to_be_clickable((By.ID, "sign-in-button")))
    submit.click()

def select_course():
    course = page_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, info["course"])))
    course.click()

def join():
    join_wait = WebDriverWait(driver, 21600) # 6 hours
    print("Waiting to join")
    join_button = join_wait.until(EC.element_to_be_clickable((By.ID, "btnJoin")))
    join_button.click()
    print("Joined")

login()
select_course()
join()

wait = WebDriverWait(driver, 21600)

while True:
    time.sleep(5)
    CURRENT_TIME = datetime.now()
    if (CURRENT_TIME.hour - START_TIME_HOUR) >= 9:
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