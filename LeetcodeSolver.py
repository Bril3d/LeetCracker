# main_script.py

import json
import logging
import clipboard
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils.utils import (
    get_element_by_xpath,
    get_elements_by_xpath,
    select_all_helper,
    paste_helper,
    sleep,
)
from Auth import login
from utils.file_manager import FileManager

IS_SOLUTION_ACCEPTED_DIV_XPATH = "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[11]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/span"
QUESTIONS_CODE_DIV_XPATH = "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[5]"
QUESTIONS_LANGUAGE_BTN_XPATH = "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[1]/div[1]/div[1]/div/div/div[1]/div/button"
QUESTIONS_LANGUAGE_DIV_XPATH = "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div"
QUESTIONS_SUBMIT_ACCEPTED_XPATH = (
    "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[4]/div/div[1]/div[1]/div[2]"
)
QUESTIONS_SUBMIT_DIV_XPATH = "/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[3]/div[3]/div/button"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LeetcodeSolver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        login(self.driver)

    def check_if_solved_earlier(self, problem_name):
        solved_problem_set = FileManager.get_solved_problem_set()
        return problem_name in solved_problem_set

    def solve_problem_with_name(self, problem_name):
        self.driver.get(f"https://leetcode.com/problems/{problem_name}")

        try:
            try:
                accepted_div = get_element_by_xpath(
                    self.driver, QUESTIONS_SUBMIT_ACCEPTED_XPATH
                )
                accepted_text = accepted_div.text
                if "Solved" in accepted_text:
                    logger.info(f"[ALREADY_SOLVED]: {problem_name}")
                    FileManager.set_solved_problem_set(problem_name)
                    return
            except Exception:
                pass

            logger.info(f"[SOLVING]: {problem_name}")
            problem_details = FileManager.get_problem_details(problem_name)
            code = problem_details["code"]
            language = problem_details["language"]

            clipboard.copy(code)

            all_languages_btn = get_element_by_xpath(
                self.driver, QUESTIONS_LANGUAGE_BTN_XPATH
            )
            all_languages_btn.click()

            all_languages_div_name = get_elements_by_xpath(
                self.driver, QUESTIONS_LANGUAGE_DIV_XPATH
            )
            for element in all_languages_div_name:
                text = element.text.strip()
                if (
                    (text == "C++" and language == "cpp")
                    or (text == "Java" and language == "java")
                    or (text == "Python" and language == "python")
                    or (text == "Python3" and language == "python3")
                    or (text == "MySQL" and language == "mysql")
                ):
                    element.click()
                    break

            sleep(1)

            code_editor = get_element_by_xpath(self.driver, QUESTIONS_CODE_DIV_XPATH)
            code_editor.click()

            select_all_helper(self.driver)
            self.driver.switch_to.active_element.send_keys(Keys.BACK_SPACE)
            paste_helper(self.driver)

            submit_btn = get_element_by_xpath(self.driver, QUESTIONS_SUBMIT_DIV_XPATH)
            submit_btn.click()

            is_solution_accepted = get_element_by_xpath(
                self.driver, IS_SOLUTION_ACCEPTED_DIV_XPATH
            )
            solution_accepted_text = is_solution_accepted.text

            if solution_accepted_text == "Accepted":
                logger.info(f"[ACCEPTED]: {problem_name}")
                FileManager.set_solved_problem_set(problem_name)
            else:
                raise Exception(
                    f"{problem_name} {solution_accepted_text}. Looks like the solution is old, contact the developer to fix this."
                )

            sleep(1)

        except Exception as e:
            logger.error(f"[FAILED]: {problem_name} {e}")

    def solve_problems(self, problem_names):
        for problem_name in problem_names:
            if not self.check_if_solved_earlier(problem_name):
                self.solve_problem_with_name(problem_name)
            else:
                logger.info(f"[SOLVED_EARLIER]: {problem_name}")

    def solve(self):
        logger.info("<<<< Starting  Solver >>>>")
        all_problems_name = FileManager.get_all_problems_names()
        self.solve_problems(all_problems_name)
        logger.info("<<<< Exiting Leetcode Solver >>>>")


if __name__ == "__main__":
    solver = LeetcodeSolver()
    solver.solve()
