# Python Exercise #054 - Adult Group

from datetime import date

adults = 0
minors = 0
for i in range(1, 8):
    birth_year = int(input(f'What year the {i}ª person born: '))

    if date.today().year - birth_year >= 21:
        adults += 1
    else:
        minors += 1

print(f'In all we had \033[1;34m{adults}\033[m adults and \033[1;34m{minors}\033[m minors')
