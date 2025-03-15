# Python Exercise #085 - Lists with even and odd numbers

nums = [[], []]

for i in range(1, 8):
    value = int(input(f'Enter the {i}º value: '))
    if value % 2 == 0:
        nums[0].append(value)
    else:
        nums[1].append(value)

print(f'The odd values entered was {sorted(nums[0])}')
print(f'The even value entered was {sorted(nums[1])}')