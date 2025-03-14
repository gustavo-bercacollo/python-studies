# Python Exercise #082 - Splitting values into multiple lists

nums = list()
odd = list()
even = list()

while True:
    value = int(input('Enter a number: '))
    nums.append(value)
    advance = str(input('Do you want continue? [Y/N] ')).strip().upper()[0]

    if value % 2 == 0:
        odd.append(value)
    else:
        even.append(value)

    if advance == 'N':
        break
print(f'The complete list is {nums}')
print(f'The odd list is {odd}')
print(f'The even list is {even}')
