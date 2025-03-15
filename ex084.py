# Python Exercise #084 - Composite List and Data Analysis

persons = []
person_heavy = []
person_light = []

while True:
    name = input('Name: ')
    weight = int(input('Weight: '))

    persons.append([weight, name ])
    persons.sort(reverse=True)

    advance = ' '
    while advance not in 'YN':
        advance = str(input('Do you want continue: [Y/N] ')).strip().upper()[0]
    if advance == 'N':
        break

for i , p in enumerate(persons):
    if persons[i][0] == persons[0][0]:
        person_heavy.append(persons[i][1])
    if persons[i][0] == persons[-1][0]:
        person_light.append(persons[i][1])


print(f'You registered {len(persons)} persons')
print(f'The heaviest weight was {persons[0][0]}, {person_heavy}')
print(f'The lighter weight was {persons[-1][0]}, {person_light}')
