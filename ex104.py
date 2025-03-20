# Python Exercise #104 - Validating Data Input in Python

def read_int(message):
    while True:
        enter_user = input(message)
        if enter_user.isnumeric():
            print(f'You entered the value {enter_user}')
            return int(enter_user)
        else:
            print('\033[31mERROR! Please enter a valid integer\033[m')


read_int('Enter a number: ')