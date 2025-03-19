# Python Exercise #094 - Joining dictionaries and lists

all_persons = []
total_ages = 0
woman_names = []
above_average = []
while True:
    person = {
        'name': str(input('Name: ')).strip(),
        'sex': ' '
    }
    while person['sex'] not in 'FM':
        person['sex'] = str(input('Sex: [F/M] ')).strip().upper()[0]

    person['age'] = int(input('Age: '))
    total_ages += person['age']
    advance = ' '
    all_persons.append(person.copy())

    while advance not in 'YN':
        advance = str(input('Do you want continue? [Y/N] ')).strip().upper()[0]

    if advance == 'N':
        break
average = total_ages / len(all_persons)
for p in all_persons:
    if p['sex'] == 'F':
        woman_names.append(p['name'])
    if p['age'] > average:
        person_above_average = {
            'name': p['name'],
            'sex': p['sex'],
            'age': p['age']
            }
        above_average.append(person_above_average.copy())

print(f'The total of people registered are {len(all_persons)}')
print(f'The average age is {average}')
print(f'The woman registered were {woman_names}')
print('List of people above average:')
for i in above_average:
    print(f'Name: {i["name"]}; Sex: {i["sex"]}; Age: {i["age"]}')

