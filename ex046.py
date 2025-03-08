# Python Exercise #046 - Countdown

from time import sleep


for i in range(10, -1, -1):
    print(f'\r{i}', end='')
    sleep(1)

print('BUM! BUM!🎆🎇🎆🎇')
