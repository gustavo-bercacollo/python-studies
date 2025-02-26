# Exercise Python #019 - Picking a Random Item from a List

from random import choice

student_1 = str(input('Enter the name of student 1: '))
student_2 = str(input('Enter the name of student 2: '))
student_3 = str(input('Enter the name of student 3: '))
student_4 = str(input('Enter the name of student 4: '))
student_5 = str(input('Enter the name of student 5: '))

students = [student_1, student_2, student_3, student_4, student_5]

student_choose = choice(students)

print(f'The student chosen was {student_choose}')