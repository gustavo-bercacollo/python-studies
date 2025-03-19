from random import randint
from time import sleep

def drawing_nums(list_nums):
    print('Drawing 5 values from list: ', end='')
    for i in range(5):
        drawn_num = randint(1, 10)
        if drawn_num % 2 == 0:
            total.append(drawn_num)
        list_nums.append(drawn_num)
        print(drawn_num, end= ' ')
        sleep(0.4)

nums = []
total = []

drawing_nums(nums)
print('. Finished!')
print(f'adding the even values of {nums}, is {sum(total)}')
