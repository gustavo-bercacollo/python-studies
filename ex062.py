first_term = int(input('First term of AP: '))
difference = int(input('Difference: '))

i = 0
term = first_term
total_terms = 10

while True:
    while i < total_terms:
        print(term, end=' -> ')
        term += difference
        i += 1

    print('PAUSE')

    extra_terms = int(input('How many more terms do you want to show? '))
    if extra_terms == 0:
        break

    total_terms += extra_terms

print(f'The progression was finish with {total_terms} shown')
