# Python Exercise #013 - Salary Adjustment

salary = float(input("Employer's salary: "))
increase = salary + (salary * (15 / 100))

print('The employer won ${:.2f}, with an increase of 15% will receive ${:.2f}'
      .format(salary, increase))