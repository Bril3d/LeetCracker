import json
import logging
import os

logger = logging.getLogger(__name__)


class FileManager:
    @staticmethod
    def get_solved_problem_set():
        try:
            with open("solved_problems.json", "r") as f:
                return set(json.load(f))
        except FileNotFoundError:
            return set()

    @staticmethod
    def set_solved_problem_set(problem_name):
        solved_set = FileManager.get_solved_problem_set()
        solved_set.add(problem_name)
        with open("solved_problems.json", "w") as f:
            json.dump(list(solved_set), f)

    @staticmethod
    def get_problem_details(problem_name):
        with open(f"problems/{problem_name}.json", "r") as f:
            return json.load(f)

    @staticmethod
    def get_all_problems_names():
        try:
            file_list = os.listdir("./problems")
            files = [file.split(".")[0] for file in file_list]
            logger.info(f"Total Problems found {len(files)}", files)
            return files
        except FileNotFoundError:
            logger.error("Problems directory not found.")
            return []