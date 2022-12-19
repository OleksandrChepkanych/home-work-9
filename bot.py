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

def parser_comand(comand_line):
    comand = comand_line.split(' ')
    if (comand[0].lower() == "good" and comand[1].lower() == "bye") or comand[0].lower() ==  "close" or comand[0].lower() == "exit":
        comand = "exit"
        return comand
    elif comand[0].lower() == "hello":
        comand = "hello"
        return comand
    elif comand[0].lower() == "add":
        comand = "add"
        name = comand[1]
        phone = comand[2]
        return comand, name, phone
    elif comand[0].lower() == "change":
        comand = "change"
        name = comand[1]
        phone = comand[2]
        return comand, name, phone
    elif comand[0].lower() == "phone":
        comand = "phone"
        name = comand[1]
        return comand, name
    elif comand[0].lower() == "show" and comand[1].lower() == "all":
        comand = "show"
        return comand
    
    return comand_line

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
        
        if len(parser_comand(comand_line)) < 2:
            comand = parser_comand(comand_line)
        elif len(parser_comand(comand_line)) == 2:
            comand = parser_comand(comand_line[0])
            name = parser_comand(comand_line[1])
        elif len(parser_comand(comand_line)) == 3:
            comand = parser_comand(comand_line[0])
            name = parser_comand(comand_line[1])
            phone = parser_comand(comand_line[2])
        else: 
            comand = parser_comand(comand_line)

        if comand == "exit":
            print("Good bye!")
            close_file(path, contacts)
            break
        elif comand == "hello":
            print("How can I help you?")
        elif comand == "add":
            handler_add_change(name, phone) if (len(name) > 2 or len(phone) > 5) else print("Give me name and phone please")
        elif comand == "change":
            handler_add_change(name, phone) if len(name) > 2 else print("Give me name")
        elif comand == "phone":
            handler_phone(comand_line) if name in contacts else print("This contact not exists. Try to add")
        elif comand == "show":
            print(contacts)
# Виклик основної функції
main()
