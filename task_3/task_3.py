import sys
from pathlib import Path
from colorama import Fore


def print_files(directory: Path, tabs_count: int = 1) -> None:
    """
    Function accepts a directory path as a command line argument and visualizes the structure of that directory,
    displaying the names of all subdirectories and files
    :param directory: Path-object to be displayed
    :param tabs_count: Number of tabs to display
    :return: None
    """
    for path in directory.iterdir():
        if path.is_file():
            path = path.relative_to(directory)
            print(Fore.GREEN + "    " * tabs_count, path)
        elif path.is_dir():
            print(Fore.BLUE + "    " * tabs_count, f"{path.relative_to(directory)}/")
            new_tabs_count = tabs_count + 1
            print_files(directory=path, tabs_count=new_tabs_count)


def main() -> None:
    path = sys.argv[1]
    directory = Path(path)
    print(Fore.BLACK + f"{directory.name}/")
    print_files(directory=directory)


if __name__ == "__main__":
    main()
