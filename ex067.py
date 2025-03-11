# Python Exercise #067 - Times Tables v3.0

while True:
    multiplication_table = int(input('What multiplication table do you want to see? (Type "-" to exit) '))
    if multiplication_table < 0 :
        break
    for i in range(1, 11):
        print(f'{multiplication_table} x {i} = {multiplication_table * i}')
print('Bye 👋👋👋')