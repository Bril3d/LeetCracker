import json
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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

    def save_scraped_solution(self, file_content):
        os.makedirs("./problems", exist_ok=True)
        with open(f"./problems/{file_content['problemName']}.json", "w") as f:
            json.dump(file_content, f)

    def scrape_and_save_code_from_submission_id(self, submission_id):
        self.driver.get(SUBMISSION_URL_TEMPLATE.format(submission_id))

        try:
            name_div = get_element_by_xpath(
                self.driver, SCRAPER_SUBMITTED_CODE_NAME_XPATH
            )
            href = name_div.get_attribute("href")
            name_div_value = href.split("/")[-2]

            language_div = get_element_by_xpath(
                self.driver, SCRAPER_SUBMITTED_CODE_LANGUAGE_XPATH
            )
            language_div_value = language_div.text

            code_div = get_element_by_xpath(
                self.driver, SCRAPER_SUBMITTED_CODE_DIV_XPATH, 10
            )

            actions = ActionChains(self.driver)
            actions.move_to_element(code_div).click().perform()

            select_all_and_copy(self.driver)

            copied_text = paste()

            file_content = {
                "problemName": name_div_value,
                "language": language_div_value,
                "code": copied_text,
            }
            self.save_scraped_solution(file_content)

        except Exception as e:
            logger.error(f"Error while scraping submission ID {submission_id}: {e}")

    def scrape_submission_ids_from_page_id(self, page_id):
        self.driver.get(PAGE_URL_TEMPLATE.format(page_id))

        try:
            rows = get_elements_by_selector(self.driver, ".text-success")
            return [row.get_attribute("href").split("/")[-2] for row in rows]

        except Exception as e:
            logger.error(
                f"Error while scraping submission IDs from page {page_id}: {e}"
            )
            return []

    def scrape_code_from_all_submissions(self):
        for page_no in range(1, 1001):
            try:
                submission_ids = self.scrape_submission_ids_from_page_id(page_no)
                logger.info(
                    f"Submission IDs fetched from page number {page_no}: {submission_ids}"
                )

                for submission_id in submission_ids:
                    self.scrape_and_save_code_from_submission_id(submission_id)

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
