# Python Exercise #074 - Largest and smallest values in a tuple

from random import randint

drawn_numbers = ()
largest = lowest = 0

for i in range(5):
    random_num = randint(1, 10)
    drawn_numbers += (random_num,)

    if i == 0:
        largest = random_num
        lowest = random_num
    if random_num > largest:
        largest = random_num
    if random_num < lowest:
        lowest = random_num

print(f'The drawn value were {drawn_numbers}')
print(f'The largest drawn value was {largest}')
print(f'The lowest drawn value was {lowest}')
