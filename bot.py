def input_error(func):
    """Перевірка вводу"""
    def error_add(comand_line):
        try:
            comand = comand_line.split(' ')
            name = comand[1]
            if comand[0] == "phone":
                return func(name)
            phone = comand[2]
            return func(name, phone)
        except KeyError:
            print("Input error. Try again")
        except ValueError:
            print("Input error. Try again")
        except IndexError:
            print("Input error. Try again")

    return error_add


def open_file(path):
    """Зчитання файлу"""
    with open(path, 'r', encoding="UTF8") as file:
        while True:
            line = file.readline()
            if not line:
                    break
            line_split = line.split(':')
            contacts[line_split[0]] = line_split[1].removesuffix('\n')
    return contacts

def close_file(path, contacts):
    """Закриття файлу"""
    with open(path, 'w', encoding="UTF8") as file:
        for name, number in contacts.items():
            file.write(f"{name}:{number}\n")

@input_error
def handler_add_change(name, phone):
    contacts[name] = phone

@input_error
def handler_phone(name):
    print(f"{name} {contacts[name]}")


"""Основна функція. Безкінечний цикл """
contacts = {}
def main():
    path = 'C:/Work Python/home-work-9/home-work-9/contact.txt'
    open_file(path)
    while True:
        comand_line = input('Input comand: ')
        comand = comand_line.split(' ')
        if (comand[0].lower() == "good" and comand[1].lower() == "bye") or comand[0].lower() ==  "close" or comand[0].lower() == "exit":
            print("Good bye!")
            close_file(path, contacts)
            break
        elif comand[0].lower() == "hello":
            print("How can I help you?")
        elif comand[0].lower() == "add":
            handler_add_change(comand_line) if (len(comand[1]) > 2 or len(comand[2]) > 5) or len(comand) > 3 else print("Give me name and phone please")
        elif comand[0].lower() == "change":
            handler_add_change(comand_line) if len(comand[1]) > 2 else print("Give me name")
        elif comand[0].lower() == "phone":
            handler_phone(comand_line) if comand[1] in contacts else print("This contact not exists. Try to add")
        elif comand[0].lower() == "show" and comand[1].lower() == "all":
            print(contacts)
# Виклик основної функції
main()
