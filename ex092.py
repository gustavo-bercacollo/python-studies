from datetime import date

worker = {
'name': input('Name: '),
'age': date.today().year - int(input('Year of birth: ')),
'work_card': int(input('Work card: (0 does not have) '))
}

if worker['work_card'] != 0:
    worker['hiring_year'] = int(input('Year of hiring: '))
    worker['salary'] = float(input('Salary: '))
    worker['retirement'] = worker['hiring_year'] + 35

print('—' * 30)
for k, v in worker.items():
    print(f'{k} is {v}')
