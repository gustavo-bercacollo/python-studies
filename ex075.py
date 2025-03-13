
nums = (
    int(input('Enter the first value: ')),
    int(input('Enter the another value: ')),
    int(input('Enter one more value: ')),
    int(input('Enter the last value: '))
)

print(f'You entered with the values: {nums}')
print(f'The value 3 appears in the {nums.index(3)}ª position'if 3 in nums else 'The number 3 does not appears')
print(f'The number 9 appears {nums.count(9)} times')
print(f'The odd values entered were: ', end='')
for i in nums:
    if i % 2 == 0:
        print(i , end= ' ')