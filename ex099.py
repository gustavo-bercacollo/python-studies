# Python Exercise #099 - Function that finds the largest

from time import sleep

def get_largest_num(* num):
    print('Analyzing the entered values...')

    count = largest_num = 0
    for i in num:
        print(i, end=' ')
        sleep(0.4)
        if count == 0:
            largest_num = i
        else:
            if i > largest_num:
                largest_num = i
            count += 1
    print(f'{len(num)}. Were entered {len(num)} values in total')
    print(f'The largest value entered was {largest_num}')
    print('-=-' * 20)


get_largest_num(2, 9, 4, 5, 7, 1)
get_largest_num(4, 7, 0)
get_largest_num(1, 2)
get_largest_num(6)
get_largest_num()
