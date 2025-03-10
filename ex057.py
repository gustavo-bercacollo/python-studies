# Python Exercise #057 - Data Validation

sex = str(input('Inform your sex [M/F]: ')).strip().upper()[0]

while sex not in 'MF':
    sex = str(input('Invalid input. Please, enter only [M/F]: ')).strip().upper()[0]

print(f'Sex {sex} registered successfully!')
