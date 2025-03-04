# Python Exercise #031 - Travel Cost

distance = float(input('\033[1;35mWhat is the distance of your trip?\033[m '))

print(f'You will start a trip of \033[1;36m{distance:.2f}km\033[m')

if distance <= 200:
    price = distance * 0.50
    print(f'The price of your ticket will be \033[1;32m${price:.2f}\033[m')
else:
    price = distance * 0.45
    print(f'The price of your ticket will be \033[1;32m${price:.2f}\033[m')