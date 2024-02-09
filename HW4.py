# додаємо декоратор для виведення помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            if "not enough values to unpack" in str(ve):
              return "WARNING MESSAGE: Enter the argument for the command"
        except UnboundLocalError:
            return "WARNING MESSAGE"
        except KeyError as ke:
            return f"WARNING MESSAGE: {ke}"
        except IndexError as ie:
            return f"WARNING MESSAGE: {ie}"
        return f"WARNING MESSAGE: please enter correct values"

    return inner

# parse_input приймає рядок вводу користувача user_input і розбиває його на слова за допомогою методу split(). 
# повертає перше слово як команду cmd та решту як список аргументів *args.
# cmd = cmd.strip().lower() видаляє зайві пробіли навколо команди та перетворює її на нижній регістр.

def parse_input(user_input):
    if not user_input:
        return "", []  # якщо юзер натисне ентер програма закінчить свою роботу

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# перевіряємо чи номер містить знак + і цифри
# далі додаємо до словника з контактами contacts
@input_error
def add_contact(args, contacts):
    name, phone = args
    if not all(char.isdigit() or char == '+' for char in phone):
        raise ValueError("Phone number should contain only digits and '+'.")
    contacts[name] = phone
    return "Contact added."


# командою ALL виводимо всі записи в словнику у відповідному форматі
def print_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# змінюємо існуючий запис, або при відсутності виводимо помилку
@input_error            
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        raise ValueError(f"Contact with name {name} not found.")
    contacts[name] = new_phone
    return f"Phone number for {name} changed."


# виводимо на екран інформацію про запис, або при відсутності виводимо помилку
@input_error        
def get_contact_phone(args, contacts):
    name, = args
    if name not in contacts:
        raise ValueError(f"Contact with name {name} not found.")
    return f"{name}'s phone number: {contacts[name]}"


# видаляємо інформацію про запис зі словника, або при відсутності виводимо помилку
@input_error
def delete_contact(args, contacts):
    name, = args
    if name not in contacts:
        raise ValueError(f"Contact with name {name} not found.")
    del contacts[name]
    return f"Contact {name} deleted."

# основна програма
def main():
    contacts = {}
    # інструкції для використання
    print("Welcome to the assistant bot!\n\
          List of commands:\n\
          add > example: add UserName Number\n\
          change > example: change UserName NEW_Number\n\
          phone > example: phone UserName\n\
          all > example: all (print all numbers)\n\
          delete > example: delete UserName\n\
          for exit > example: \"close\" or \"exit\" or \"quit\" or \"press Enter\"")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if not command or command in ["close", "exit", "quit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print_all_contacts(contacts)
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()