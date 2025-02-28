# Python Exercise #028 - Guessing Game v.1.0
from random import randint
from time import sleep

random_number = randint(1, 5)

print(f'''
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
I'll think of a number from 0 to 5, try to guess...
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-''')

number_choose = int(input('What number i am thinking of? ').strip())
print('PROCESSING...')
sleep(2)

if random_number == number_choose:
    print('CONGRATULATIONS, you beat me!')
else:
    print(f"I WIN! I thought of the number {random_number}, not {number_choose}.")




