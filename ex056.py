# Python Exercise #056 - Complete Analyzer

ages_group = 0
oldest_man = None
oldest_age = 0
women_under_20 = 0

for i in range(1, 5):
    print(f'-------- {i}ª Person --------')
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    sex = str(input('Sex [F/M]: ')).upper().strip()

    ages_group += age

    if sex == 'M' and age > oldest_age:
        oldest_age = age
        oldest_man = name
    if sex == 'F' and age < 20:
        women_under_20 += 1


print(f'The average age is {ages_group / 4}')
print('No man was informed') if oldest_man is None else print(f'The oldest man\'s age is {oldest_age} and his name is {oldest_man}' )
print(f'Total of {women_under_20} women under 20 years old') if women_under_20 > 0 else print('No woman was informed')


