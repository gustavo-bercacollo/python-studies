# Python Exercise #087 - More about Arrays in Python

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
odd_nums_total = third_column_total = 0
largest_value_second_row = ' '
''
for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f'Enter the value to [{i},{j}]: '))

for i in range(3):
    for j in range(3):
        print(f'[{matrix[i][j]:^5}]', end='')
        if matrix[i][j] % 2 == 0:
            odd_nums_total += matrix[i][j]
        if j == 2:
            third_column_total += matrix[i][j]
        if i == 1 and j == 0:
            largest_value_second_row = matrix[i][0]
        if i == 1:
            if matrix[i][j] > largest_value_second_row:
                largest_value_second_row = matrix[i][j]

    print()
print(odd_nums_total, third_column_total, largest_value_second_row)
print(f'The sum of the odd values is {odd_nums_total}')
print(f'The total of the third column is {third_column_total}')
print(f'The largest value of the second row is {largest_value_second_row}')
