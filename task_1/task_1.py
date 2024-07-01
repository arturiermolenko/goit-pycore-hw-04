import re
from typing import Tuple, List


def file_to_list(lines: List[str]) -> List[int] | None:
    """
    Function takes list of strings that contains name and salary and returns list of salaries
    :param lines: List of strings with names and salaries
    :return: list of salaries as integers
    """
    pattern = r"^[a-zA-Z0-9 -]+,[a-zA-Z0-9 -]+$"
    salary_list = []
    for number, line in enumerate(lines):
        if not re.match(pattern=pattern, string=line):
            print(f"Check the input file. String #{number + 1} is in incorrect format!")
            return
        salary = int(line.split(",")[1].strip())
        salary_list.append(salary)

    return salary_list


def total_salary(path: str) -> Tuple[int, int] | None:
    """
    Function parses file and returns the total and average salary of all developers
    :param path: String, path to the file
    :return: tuple of 2 values : the total and average salary
    """

    try:
        with open(path, "r", encoding="UTF-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("There is no such file. Check the path please")
        return

    salary_list = file_to_list(lines)

    if salary_list:
        total_salary_value = sum(salary_list)
        average_salary_value = int(total_salary_value / len(salary_list))

        return total_salary_value, average_salary_value
    return


if __name__ == "__main__":
    try:
        total, average = total_salary("task_1/salary.txt")
    except TypeError:
        ...
    else:
        print(f"The total salary is: {total}, the average salary is: {average}")
