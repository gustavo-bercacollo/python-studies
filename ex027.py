# Exercise Python #027 - First and Last Name of a Person

full_name = str(input('Enter your full name: ')).strip()

firth_name = full_name.split()[0]
second_name = full_name.split()[-1]

print(f'''
    Nice to meet you!
    Your firth name is {firth_name}
    Your second name is {second_name}
    ''')