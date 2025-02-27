# Exercise Python #023 - Separating Digits from a Number

number = int(input('Enter with a number: '))
unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
mile = number // 1000 % 10

print(
    f'''
    Analyzing the number: {number}...
    Unit: {unit}
    Ten: {ten}
    Hundred: {hundred}
    Mile: {mile}
    ''')