# Exercise Python #016 - Breaking a Number

from math import trunc

user_enter = float(input('Enter with a number: '))

print('The value entered was {} and its entire portion is {}'. format(user_enter, trunc(user_enter)))