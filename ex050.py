# Python Exercise #050 - Sum of evens

total = 0
count = 0
for i in range(1,7):
    num = int(input(f'Enter the {i} value: '))
    if num % 2 == 0:
        total += num
        count += 1
print(f'You entered {count} even value and the sum was {total}') \
    if count == 1 else print(f'You entered {count} even values and the sum was {total}')

