# Python Exercise #113 - Functions in Python in depth

while True:
    try:
        int_num = int(input('Enter an integer number: '))
        break
    except ValueError:
        print('\033[31mError: Please enter a valid integer number.\033[m')
    except KeyboardInterrupt:
        print('\n\033[31mError: The user chose not to enter the data. Exiting...\033[m')

while True:
    try:
        real_num = float(input('Enter a real number: '))
        break
    except ValueError:
        print('\033[31mError: Please enter a valid real number.\033[m')
    except KeyboardInterrupt:
        print('\n\033[31mError: The user chose not to enter the data. Exiting...\033[m')

print(f'The integer number entered was {int_num} and the real number was {real_num}.')
