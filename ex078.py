#Python Exercise #078 - Largest and Smallest Values ​​in List

num = []

largest = lowest = 0
largest_positions = []
lowest_positions = []

for i in range(0, 5):
    num.append(int(input(f'type a number to the index {i}: ')))
    if i == 0:
        largest = lowest = num[i]
    if num[i] > largest:
        largest = num[i]
    if num[i] < lowest:
        lowest = num[i]
for i, n in enumerate(num):
    if largest == n:
        largest_positions.append(i)
    if lowest == n:
        lowest_positions.append(i)
print('*' * 50)
print(f'You entered with the values {num}')
print(f'The largest value entered was {largest} in the positions {largest_positions}')
print(f'The lowest value entered was {lowest} in the positions {lowest_positions}')
