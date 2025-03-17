
student = dict()
student['name'] = input('Name: ')
student['average'] = float(input('Average: '))
student['situation'] = 'approved' if student['average'] >= 7 else 'recovery' if student['average'] >= 5 else 'failed'

for k, v in student.items():
    print(f'— The {k} is {v}')
