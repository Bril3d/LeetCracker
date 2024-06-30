import os
import time
import json
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()

def save_cookies(driver, cookies_path):
    with open(cookies_path, 'w') as file:
        json.dump(driver.get_cookies(), file)

def load_cookies(driver, cookies_path):
    with open(cookies_path, 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

def login(driver):
    cookies_path = "cookies.json"
    driver.get("https://leetcode.com/accounts/login/")
    
    if os.path.exists(cookies_path):
        load_cookies(driver, cookies_path)
        driver.refresh()
        time.sleep(5)
        if driver.current_url == "https://leetcode.com/accounts/login/":
            print("Cookies expired, performing login")
        else:
            print("Logged in using cookies")
            return
    else:
        print("Cookies not found, performing login")
    
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
    
    if driver.current_url != "https://leetcode.com/accounts/login/":
        save_cookies(driver, cookies_path)
        print("Login successful, cookies saved")
    else:
        print("Login failed")
