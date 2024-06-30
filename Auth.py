import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import time

load_dotenv()

def login(driver):
    driver.get("https://leetcode.com/accounts/login/")
    time.sleep(15)  

    username_input = driver.find_element(By.ID, "id_login")
    password_input = driver.find_element(By.ID, "id_password")
    login_button = driver.find_element(By.ID, "signin_btn")

    username = os.getenv("LEETCODE_USERNAME")
    password = os.getenv("LEETCODE_PASSWORD")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(10) 
