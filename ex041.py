# Python Exercise #041 - Classifying Athletes

from datetime import date

birth_year = int(input('Year of birth: '))
years_old = date.today().year - birth_year

print(f'The athlete have {years_old} years old')

if years_old <= 9:
    print('Classification: Kid')
elif years_old <= 14:
    print('Classification: Childish')
elif years_old <= 19:
    print('Classification: Junior')
elif years_old <= 25:
    print('Classification: Senior')
else:
    print('Classification: Master')