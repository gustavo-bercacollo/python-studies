# Python Exercise #048 - Sum of odd multiples of three

sum_odd = 0
value = 0
for i in range (1, 501):
    if i % 2 == 1 and i % 3 == 0:
        sum_odd += i
        value += 1

print(f'The sum of {value} request values is {sum_odd} ')
