# Python Exercise #106 - Interactive Python Help System

from time import sleep

def help_system():
    while True:
        print('\033[42m~~~~~~~~~~~~~~~~~~~~~~\033[m')
        print('\033[42m HELP SYSTEM PyHELP   \033[m')
        print('\033[42m~~~~~~~~~~~~~~~~~~~~~~\033[m')

        enter_user = input('Function or library > ').strip().lower()
        if enter_user == 'end':
            break

        phrase = 'accessing the command manual'
        print('\033[44m~\033[m' * (len(phrase) + len(enter_user) + 5 ))
        print(f'\033[44m  {phrase} {enter_user}  \033[m')
        print('\033[44m~\033[m' * (len(phrase) + len(enter_user) + 5))
        sleep(2)
        print(f'\033[7m{eval(enter_user).__doc__}\033[m')
        sleep(3)
    print('\033[41m~~~~~~~~~~~~~~~~~~\033[m')
    print('\033[41m  SEE YOU LATTER  \033[m')
    print('\033[41m~~~~~~~~~~~~~~~~~~\033[m')
help_system()