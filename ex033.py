# Python Exercise #033 - Largest and smallest values

num1 = int(input('Enter the first value: '))
num2 = int(input('Enter the second value: '))
num3 = int(input('Enter the third value: '))

num_list = [num1, num2, num3]

largest = max(num_list)
smallest = min(num_list)

print(f'The largest value is \033[1;34m{largest}\033[m\n'
      f'The smallest value is \033[1;34m{smallest}\033[m')
