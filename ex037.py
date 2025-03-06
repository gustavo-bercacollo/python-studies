# Python Exercise #037 - Number Base Converter

int_number = int(input('Enter int number: '))

menu = int(input(('''
    [1] Convert to binary  
    [2] Convert to octagonal
    [3] Convert to hexadecimal
    Your option: ''')))

if menu == 1:
    print(f'{int_number} converted to binary is iqual to {bin(int_number)[2:]}')
elif menu == 2:
    print(f'{int_number} converted to octagonal is iqual to {oct(int_number)[2:]}')
elif menu == 3:
    print(f'{int_number} converted to hexadecimal is iqual to {hex(int_number)[2:]}')
else:
    print('Option invalid!\n'
          'Please, enter with 1, 2 or 3')
