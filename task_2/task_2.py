import re
from typing import List, Dict


def file_to_list(lines: List[str]) -> List[List[str | int]] | None:
    """
    Function takes list of strings that contains id, name and age of each cat 
    and returns list correctly formated lists with info about cat
    :param lines: List of strings 
    :return: list of lists
    """
    pattern = r"^[a-zA-Z0-9]+,[a-zA-Z0-9 -]+,[0-9]+$"
    salary_list = []
    for number, line in enumerate(lines):
        if not re.match(pattern=pattern, string=line):
            print(f"Check the input file. String #{number + 1} is in incorrect format!")
            return
        cat_info = line.split(",")
        cat_info[-1] = int(cat_info[-1].strip())
        salary_list.append(cat_info)

    return salary_list


def get_cats_info(path: str) -> List[Dict] | None:
    """
    Function reads a file and returns a list of dictionaries with information about each cat
    :param path: String, path to the file
    :return: list of dictionaries with info about each cat
    """

    try:
        with open(path, "r", encoding="UTF-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("There is no such file. Check the path please")
        return

    list_of_cat_lists = file_to_list(lines)
    list_of_cat_dicts = []

    if list_of_cat_lists:
        for cat in list_of_cat_lists:
            cat_dict = {
                "id": cat[0],
                "name": cat[1],
                "age": cat[2]
            }
            list_of_cat_dicts.append(cat_dict)

    return list_of_cat_dicts


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
