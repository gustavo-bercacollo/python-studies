# Python Exercise #083 - Validating mathematical expressions

expression = list()
open_parentheses = close_parentheses = 0

user_enter = expression.append(str(input('Enter an expression: ')).strip())

for i in expression:
    for j in i:
        if j == '(':
            open_parentheses += 1
        if j == ')':
            close_parentheses += 1

if open_parentheses == close_parentheses:
    print('Your expression is correct!')
else:
    print('Your expression is wrong!')