def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid index provided."

    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args, contacts):
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone} \n"
    return result.strip()

# Додайте інші функції для обробки інших команд

while True:
    command = input("Enter a command: ").lower()
    
    if command == "add":
        args = input("Enter the argument for the command: ").split()
        print(add_contact(args, contacts))
    elif command == "phone":
        args = input("Enter the argument for the command: ").split()
        print(get_phone(args, contacts))
    elif command == "all":
        args = input("Enter the argument for the command: ").split()
        print(show_all(args, contacts))
    else:
        print("Invalid command. Please enter 'add', 'phone', or 'all'.")
