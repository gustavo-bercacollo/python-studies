
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f'Enter the value to [{i},{j}]: '))

for i in range(3):
    for j in range(3):
        print(f'[{matrix[i][j]:^5}]', end='')
    print()
