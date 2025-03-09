# first termPython Exercise #051 - Arithmetic Progression

first_term = int(input('First term of AP: '))
difference = int(input('Difference: '))
tenth_term = first_term + (10 - 1) * difference

for i in range(first_term, tenth_term + difference, difference):
   print( i, end='-> ')
print('END')