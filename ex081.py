# Python Exercise #081 - Extracting data from a List

nums = []

while True:
    nums.append(int(input('Enter a number: ')))
    advance = str(input('Do you want continue? [Y/N] ')).strip().upper()[0]

    if advance == 'N':
        break

print(f'You entered with {len(nums)} elements')
print(f'The values in decreasing order are {sorted(nums, reverse=True)}')
print('The value 5 is in the list') if 5 in nums else print('The value 5 is not in the list')

