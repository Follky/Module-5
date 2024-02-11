def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please provide valid command."
        except ValueError:
            return "Please provide valid input."

    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def remove_contact(args, contacts):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact removed."
    else:
        return "Contact not found."

@input_error
def list_contacts(args, contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available."

def handle_command(command, contacts):
    parts = command.split()
    if not parts:
        return "Please enter a command."
    
    if parts[0] == "add":
        if len(parts) == 3:
            return add_contact(parts[1:], contacts)
        else:
            return "Usage: add <name> <phone>"
    
    elif parts[0] == "get":
        if len(parts) == 2:
            return get_contact(parts[1:], contacts)
        else:
            return "Usage: get <name>"
    
    elif parts[0] == "remove":
        if len(parts) == 2:
            return remove_contact(parts[1:], contacts)
        else:
            return "Usage: remove <name>"
    
    elif parts[0] == "list":
        return list_contacts(parts[1:], contacts)
    
    else:
        return "Invalid command. Available commands: add, get, remove, list"

def main():
    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            break
        response = handle_command(command, contacts)
        print(response)

if __name__ == "__main__":
    main()
