import time
import clipboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def get_element_by_xpath(driver, xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

def get_elements_by_xpath(driver, xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    

def get_elements_by_selector(driver, selector, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
    )

def select_all_helper(driver):
    driver.execute_script("document.execCommand('selectAll', false, null)")
    
def select_all_and_copy(driver):
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

def paste():
    return clipboard.paste()
  
def paste_helper(driver):
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

def sleep(seconds):
    time.sleep(seconds)
