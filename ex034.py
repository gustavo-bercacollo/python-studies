# Python Exercise #034 - Multiple Augmentations

salary = float(input("What is the employer's salary? "))

if salary >= 1250:
    new_salary = (salary * 10/100) + salary
    print(f'Who earned \033[1;31m${salary:.2f}\033[m will receive \033[1;32m${new_salary:.2f}\033[m')
else:
    new_salary = (salary * 15 / 100) + salary
    print(f'Who earned \033[1;31m${salary:.2f}\033[m will receive \033[1;32m${new_salary:.2f}\033[m')
