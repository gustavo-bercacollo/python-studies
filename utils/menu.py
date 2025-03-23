from time import sleep
from utils.file import create_file, exist_file, read_file, register_new_person
from utils.helpers import format_title

cols = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'reset': '\033[m'
}

file_name = 'people_list.txt'
if not exist_file(file_name):
    create_file(file_name)


def show_menu():
    format_title('MAIN MENU')
    print(f"{cols['yellow']}1{cols['reset']} - {cols['blue']}Show people registered{cols['reset']}")
    print(f"{cols['yellow']}2{cols['reset']} - {cols['blue']}Register new person{cols['reset']}")
    print(f"{cols['yellow']}3{cols['reset']} - {cols['blue']}Exit{cols['reset']}")
    print('—' * 30)

def user_option():
    while True:
        try:
            enter_user = int(input('\033[33mYour option:\033[m '))
            match enter_user:
                case 1:
                    format_title('OPTION 1')
                    read_file(file_name)
                    sleep(2)
                    show_menu()
                case 2:
                    format_title('NEW REGISTER')
                    while True:
                        try:
                            name = str(input('Name: '))
                            if not name.isalpha():
                                raise ValueError('The name must be alphabetical')
                            break
                        except ValueError as error:
                            print(f'{cols['red']}Error: Invalid name. {error}{cols['reset']}')
                    while True:
                        try:
                            age = input('Age: ').strip()
                            if not age.isnumeric():
                                raise ValueError('The age must be a number')

                            age = int(age)
                            if age <= 0:
                                raise ValueError("Age must be a positive number.")

                            break
                        except ValueError as error:
                            print(f"{cols['red']}Error: Invalid age. {error}{cols['reset']}")

                    register_new_person(file_name, name, age)
                    sleep(2)
                    show_menu()
                case 3:
                    format_title('Exiting...')
                    break
                case _:
                    print(f"{cols['red']}Error: Invalid option. Please choose 1, 2, or 3.{cols['reset']}")

        except ValueError:
            print(f"{cols['red']}Error: Please, enter a valid integer number.{cols['reset']}")
