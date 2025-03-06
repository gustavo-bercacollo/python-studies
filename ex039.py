# Python Exercise #039 - Military Enlistment

from datetime import date

birth_year = int(input('What year were you born? '))
current_year = date.today().year
years_old = current_year - birth_year

print(f'You have {years_old} yeas old')

if years_old < 18:
    enlistment = 18 - years_old
    print(f'There are still {enlistment} years left until enlistment') if enlistment > 1 else\
    print(''f'There are still {enlistment} year left until enlistment')
    print(f'Your enlistment will be in {current_year + enlistment}')
elif years_old > 18:
    enlistment =  years_old - 18
    print(f'you should have enlisted {enlistment} years ago') if enlistment > 1 else \
    print(''f'you should have enlisted {enlistment} year ago')
    print(f'Your enlistment was in {current_year - enlistment}')
else:
    print('enlist immediately!'.upper())
