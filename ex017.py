# Exercise Python #017 - Legs and Hypotenuse

from math import hypot
opposite_side = float(input('Enter the length of opposite side: '))
adjacent_side = float(input('Enter the length of adjacent side: '))
hypotenuse = hypot(opposite_side, adjacent_side)

print('The value of hypotenuse is {:.2f}'.format(hypotenuse))
