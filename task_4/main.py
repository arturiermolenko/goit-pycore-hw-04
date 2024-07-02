from handlers import add_contact, change_contact, print_contact


def parse_input(user_input):
    """Take users input as a string and split into separate command and list of args"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def print_hint():
    print(
        """
            Type 'add name phone' to add a new contact.
            Type 'change contact phone' to change contact.
            Type 'phone name' to print contacts phone number.
            Type 'all' to print all contacts in phone book
            Type 'close' or 'exit' to exit the assistant. 
            """
    )


def main():
    contacts = {}
    print(
        """
    Hello. Welcome to the assistant bot!
    Type 'hello' to interact with the bot.
    """
    )
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("Not a valid command. Check it, please!")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
            print_hint()
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(print_contact(args, contacts))
        elif command == "all":
            for username, phone in contacts.items():
                print(f"{username}: {phone}")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
