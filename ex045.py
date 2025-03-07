# Python Exercise #045 - GAME: Rock, Paper, Scissors

from random import randint
from time import sleep

items = ('Rock', 'Paper', 'Scissor')

player_move = int(input('''
Rock, Paper, Scissors 🤚✌️👊
[0] Rock
[1] Paper
[2] Scissor
What is your move? '''))

computer_move = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('=-' * 15)
print(f'The Computer played {items[computer_move]}\n'
      f'The Player played {items[player_move]}')
print('=-' * 15)

if computer_move == 0:
    if player_move == 0:
        print('TIE')
    elif player_move == 1:
        print('PLAYER WINS')
    elif player_move == 2:
        print('COMPUTER WINS')
elif computer_move == 1:
    if player_move == 0:
        print('COMPUTER WINS')
    elif player_move == 1:
        print('TIE')
    elif player_move == 2:
        print('PLAYER WINS')
if computer_move == 2:
    if player_move == 0:
        print('PLAYER WINS')
    elif player_move == 1:
        print('COMPUTER WINS')
    elif player_move == 2:
        print('TIE')


