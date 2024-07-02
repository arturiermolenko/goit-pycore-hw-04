import re
from typing import List


def check_args(args: List[str]):
    name_pattern = r"^[A-Za-z]+$"
    phone_pattern = r"^\+380\d{9}$"
    if len(args) != 2:
        return "Invalid number of arguments. Please provide name and phone number."
    elif not re.match(name_pattern, args[0]) or not re.match(phone_pattern, args[1]):
        return """
        Invalid input. 
        Name should contain only alphanumeric characters.
        Phone number should be in format: +380XXXXXXXXX.
        """


def add_contact(args, contacts):
    """Add a contact to the dict of contacts"""
    check_args(args)
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Change a contact in the dict of contacts"""
    check_args(args)
    name, phone = args
    contact = contacts.get(name)
    if contact:
        contacts[name] = phone
        return "Contact changed."
    return "Contact not found."


def print_contact(args: List, contacts):
    """Print a single contact from the dict of contacts"""
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return "Contact not found."
