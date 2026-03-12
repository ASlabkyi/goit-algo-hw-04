def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return "Contact already exist. Please use 'change' to change your phone number."
        contacts[name] = phone
    except ValueError:
        return "Input error! Use format: cmd name number."
    return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name not in contacts:
            return "Contact not found."
        contacts[name] = phone
    except ValueError:
        return "Input error! Use format: cmd name number."
    return "Contact changed."

def contact_phone(args, contacts):
    if len(args) != 1:
        return "Input error! Use format: cmd name."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all_contacts(contacts):
    result = []
    if len(contacts) == 0:
        return "No contacts found."
    for name in sorted(contacts):
        phone = contacts[name]
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
        cmd, *args = parse_input(user_input)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(contact_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()