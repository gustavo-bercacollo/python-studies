# Python Exercise #040 - That Classic Average

first_grade = float(input('First grade: '))
second_grade = float(input('Second grade: '))

average = (first_grade + second_grade) / 2

print(f'Taking {first_grade} and {second_grade}, your average is {average:.2f}')

if average < 5:
    print('Failed')
elif 5 <= average < 7:
    print('Recovery')
else:
    print('Approved!')
