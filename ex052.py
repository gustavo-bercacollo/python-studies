num = int(input('Enter with a number: '))

count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
        print(f'\033[33m{i}\033[m', end=' ')
    else:
        print(f'\033[31m{i}\033[m', end=' ')

if count == 2:
    print(f'\nThe number {num} was divided {count} times\nIt is not a prime number.')
else:
    print(f'\nThe number {num} was divided {count} times \nIt is a prime number.')