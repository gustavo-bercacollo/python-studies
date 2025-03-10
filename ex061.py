# first termPython Exercise #061 - Arithmetic Progression v.2.0

first_term = int(input('First term of AP: '))
difference = int(input('Difference: '))

i = 0
term = first_term

while i < 10:
    print(term, end=' -> ')
    term += difference
    i += 1

print('END')


'''for i in range(first_term, tenth_term + difference, difference):
   print( i, end='-> ')
print('END')'''