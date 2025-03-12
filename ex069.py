# Python Exercise #069 - Group Data Analysis

total_major = total_man = total_woman = 0

while True:
    print(f'{' Register a person ':—^50}')
    while True:
        age = int(input('Age: '))
        if age >= 0:
            break
    sex = ' '
    while sex not in 'MF':
     sex = str(input('Sex: [M/F] ')).strip().upper()[0]
    print('—' * 20)
    advance = ' '
    while advance not in 'SN':
       advance = str(input('Do you want continue? [S/N] ')).strip().upper()[0]

    if age > 18:
        total_major += 1
    if sex == 'F' and age < 20:
        total_woman += 1
    if sex == 'M':
        total_man += 1
    if advance == 'N':
        break
print(f'Total number of people over 18 years old: {total_major}')
print(f'In total we have {total_man} mens registered')
print(f'And we have {total_woman} women registered under 20 years old')



