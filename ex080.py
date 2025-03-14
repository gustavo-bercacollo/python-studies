#Python Exercise #080 - Ordered list without repetitions

nums = []

for i in range(5):
    value = int(input('Enter with a value: '))

    if i == 0 or value > nums[-1]:
        nums.append(value)
        print('Adding the value in the end of the list...')
    else:
        i = 0
        while i < len(nums):
            if value <= nums[i]:
                nums.insert(i, value)
                print(f'Adding the value in the position {i} of the list...')
                break
            i += 1
print(nums)

