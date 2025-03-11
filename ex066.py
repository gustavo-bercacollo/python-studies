# Python Exercise #066 - Multiple numbers with flag

total = counter = 0
while True:
    num = int(input('Enter with a value (999 to stop): '))
    if num == 999:
        break
    total += num
    counter += 1

print(f'The sum of {counter} values is {total}')
