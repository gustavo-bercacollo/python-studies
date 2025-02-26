# Exercise Python #020 - Randomizing the Order of a List

from random import shuffle

student_1 = str(input('Enter the name of student 1: '))
student_2 = str(input('Enter the name of student 2: '))
student_3 = str(input('Enter the name of student 3: '))
student_4 = str(input('Enter the name of student 4: '))
student_5 = str(input('Enter the name of student 5: '))

students = [student_1, student_2, student_3, student_4, student_5]

shuffle(students)

print(f'The presentation order will be {students}')