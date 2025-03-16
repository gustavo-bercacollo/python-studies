# Python Exercise #088 - Lottery Predictions

from random import randint
from time import sleep

draw_nums_temp = []
all_draw_nums = []

nums_of_games = int(input('How many games do you want to draw? '))
print(f'{f" DRAWING {nums_of_games} GAMES ":~^40}')

for i in range(1, nums_of_games + 1):
    for j in range(6):
        random_nums = randint(1, 60)
        draw_nums_temp.append(random_nums)

    print(f'Game {i}: {draw_nums_temp}')
    sleep(1)
    all_draw_nums.append(draw_nums_temp[:])
    draw_nums_temp.clear()
print(all_draw_nums)