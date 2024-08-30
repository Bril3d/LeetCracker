import json
import os
import logging
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor
from utils.utils import (
    get_element_by_xpath,
    get_elements_by_selector,
    select_all_and_copy,
    paste,
)
from Auth import login

SCRAPER_SUBMITTED_CODE_DIV_XPATH = "/html/body/div[2]/div/div[1]/div/div[2]/div[7]/div/div[3]/div/div/div[3]/div/div[3]/div[1]"
SCRAPER_SUBMITTED_CODE_LANGUAGE_XPATH = (
    "/html/body/div[2]/div/div[1]/div/div[2]/div[7]/div/div[1]/div/div[1]/span"
)
SCRAPER_SUBMITTED_CODE_NAME_XPATH = "/html/body/div[2]/div/div[1]/div/div[1]/h4/a"
SUBMISSION_URL_TEMPLATE = "https://leetcode.com/submissions/detail/{}"
PAGE_URL_TEMPLATE = "https://leetcode.com/submissions/#/{}"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LeetcodeScraper:

    def __init__(self):
        self.driver = webdriver.Chrome()
        login(self.driver)
        self.session = requests.Session()
        for cookie in self.driver.get_cookies():
            self.session.cookies.set(cookie['name'], cookie['value'])

    def save_scraped_solution(self, file_content):
        os.makedirs("./problems", exist_ok=True)
        with open(f"./problems/{file_content['problemName']}.json", "w") as f:
            json.dump(file_content, f)

    def scrape_and_save_code_from_submission_id(self, submission_id):
        url = SUBMISSION_URL_TEMPLATE.format(submission_id)
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            name_div = soup.select_one(SCRAPER_SUBMITTED_CODE_NAME_XPATH)
            href = name_div['href']
            name_div_value = href.split("/")[-2]

            language_div = soup.select_one(SCRAPER_SUBMITTED_CODE_LANGUAGE_XPATH)
            language_div_value = language_div.text

            code_div = soup.select_one(SCRAPER_SUBMITTED_CODE_DIV_XPATH)
            copied_text = code_div.text
            file_content = {
                "problemName": name_div_value,
                "language": language_div_value,
                "code": copied_text,
            }
            self.save_scraped_solution(file_content)

        except Exception as e:
            logger.error(f"Error while scraping submission ID {submission_id}: {e}")

    def scrape_submission_ids_from_page_id(self, page_id):
        url = PAGE_URL_TEMPLATE.format(page_id)
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            rows = soup.select(".text-success")
            return [row['href'].split("/")[-2] for row in rows]
        except Exception as e:
            logger.error(f"Error while scraping submission IDs from page {page_id}: {e}")
            return []
    def scrape_code_from_all_submissions(self):
        with ThreadPoolExecutor(max_workers=5) as executor:
            for page_no in range(1, 1001):
                try:
                    submission_ids = self.scrape_submission_ids_from_page_id(page_no)
                    logger.info(f"Submission IDs fetched from page number {page_no}: {submission_ids}")
                    if not submission_ids:
                        break

                    futures = [executor.submit(self.scrape_and_save_code_from_submission_id, submission_id) 
                               for submission_id in submission_ids]

                    for future in futures:
                        future.result()

                except Exception as e:
                    logger.error(f"Error in page {page_no}: {e}")
                    break
    def scrape_accepted_solutions(self):
        logger.info("<<<< Starting Leetcode Scraper >>>>")
        self.scrape_code_from_all_submissions()
        logger.info("<<<< Exiting Leetcode Scraper >>>>")

if __name__ == "__main__":
    scraper = LeetcodeScraper()
    scraper.scrape_accepted_solutions()
