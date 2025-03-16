# Python Exercise #089 - Bulletin with compound lists

from time import sleep

students = []

while True:
    temp = [str(input('Name: ')), float(input('Grade 1: ')), float(input('Grade 2: '))]

    students.append(temp[:])
    temp.clear()

    advance = ' '
    while advance not in 'YN':
        advance = str(input('Do you want continue? [Y/N] ')).strip().upper()[0]
    if advance == 'N':
        break

print('-' * 50)
print(f"{'ID':<4}{'NAME':<10}{'AVERAGE':>8}")
print('-' * 50)

for i, student in enumerate(students):
    print(f'{i:<4} {student[0]:<10} {(student[1] + student[2]) / 2:>8.1f}')
print('—' * 50)

while True:
    student_id = int(input('Show what student grande? (999 to cancel) '))
    if student_id == 999:
        break
    if 0 <= student_id < len(students):
        print(f"{students[student_id][0]}'s grade are {students[student_id][1]} and {students[student_id][2]} ")
    else:
        print("Invalid student ID. Try again.")
print('CANCELLING...')
sleep(1)
print('Bye👋')