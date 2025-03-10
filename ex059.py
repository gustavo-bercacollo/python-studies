
from time import sleep

num_1 = int(input('First value: '))
num_2 = int(input('Second value: '))

user_option = 0
while user_option != 5:
    print(  '[ 1 ] Sum\n'
            '[ 2 ] Multiply\n'
            '[ 3 ] Largest\n'
            '[ 4 ] New values\n'
            '[ 5 ] Exit')
    user_option = int(input('>>>>> What is your option? '))

    if user_option == 1:
        total = num_1 + num_2
        print(f'\033[1;33mSum between {num_1} and {num_2} is {total}\033[m')
        print('-==' * 15)
    elif user_option == 2:
        total = num_1 * num_2
        print(f'\033[1;33mThe multiplication between {num_1} and {num_2} is {total}\033[m')
        print('-==' * 15)
    elif user_option == 3:
        if num_1 > num_2:
            print(f'\033[1;33mBetween {num_1} and {num_2} the largest is {num_1}\033[m')
            print('-==' * 15)
        else:
            print(f'\033[1;33mBetween {num_1} and {num_2} the largest is {num_2}\033[m')
            print('-==' * 15)
    elif user_option == 4:
        print('-==' * 15)
        print('Enter with new values')
        num_1 = int(input('First value: '))
        num_2 = int(input('Second value: '))
    elif user_option == 5:
        print('bye 👋👋👋')
    else:
        print('\033[1;31mInvalid enter. Please, enter with 1-5 🤗\033[m')

    # Loading effect
    sleep(2.5)
    print('\033[1;32mLoading menu\033[m', end='')
    sleep(1)
    print('\033[1;32m.\033[m', end='')
    sleep(1)
    print('\033[1;32m.\033[m', end='')
    sleep(1)
    print('\033[1;32m.\033[m')
    sleep(0.5)

