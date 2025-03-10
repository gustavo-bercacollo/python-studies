
from random import randint

computer_guess = randint(0, 10)

print('I just thought of a number from 0 to 10\nYou can guess what number is it?')

player_guess = int(input('What is your guess? '))

counter = 1
while player_guess != computer_guess:
    counter += 1
    if computer_guess > player_guess:
        print('Higher..., try again.')
        player_guess = int(input('What is your guess? '))
    else:
        print('Lower..., try again.')
        player_guess = int(input('What is your guess? '))

print(f'You got it right!! with {counter} tries, congratulations!')