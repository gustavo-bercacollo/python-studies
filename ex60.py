# Python Exercise #060 - Factorial Calculation

# using for
num = int(input('Enter with a number to see you factorial: '))

print(f'{num}! = ', end='')

factorial = 1
for i in range(num, 0, -1):
    print(i, end=' x ' if i > 1 else ' = ')
    factorial *= i

print(factorial)


# using while
'''num = int(input('Enter with a number to see you factorial: '))

print(f'{num}! = ', end='')

factorial = 1
i = num
while i > 0:
    print(i, end=' x ' if i > 1 else ' = ')
    factorial *= i
    i -= 1
print(factorial)'''