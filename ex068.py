
from random import randint

computer_move_number = randint(0, 10)

print(f'{" Let's play odd and even! ":—^50}')

counter = 0

while True:
    player_move_number = int(input('Play a value: '))
    player_move = str(input('Odd or even? [O/E] ')).strip().upper()[0]

    total = player_move_number + computer_move_number


    if total % 2 == 0:
        odd_or_even = 'ODD'
    else:
        odd_or_even = 'EVEN'

    print('—' * 50)
    print(f'You played {player_move_number} and the computer {computer_move_number}. Total of {total}. {odd_or_even}')
    print('—' * 50)

    if odd_or_even == 'ODD' and player_move == 'O' or odd_or_even == 'EVEN' and player_move == 'E':
        print('YOU WIN!\n'
              'Let\'s play again...')
        print('—' * 15)
        counter += 1
    else:
        print(f'GAME OVER!👾 You win {counter} times')

        break


