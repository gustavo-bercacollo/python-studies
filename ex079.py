
nums = []

while True:
    value = int(input('Enter with a value: '))
    if value not in nums:
        nums.append(value)
        print('Value add with success!')
    else:
        print('Duplicated value. Value not add')
    advance = ' '
    while advance not in 'NS':
        advance = str(input('Do you want continue? [S/N] ')).strip().upper()[0]
    if advance == 'N':
        break
print(f'You entered with the values {sorted(nums)}')
