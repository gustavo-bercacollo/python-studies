# Python Exercise #044 - Payment Manager

print(f"{' SHOPPING MALL ':=^40}")
price = float(input('Shopping prices: $'))

menu = int(input('''
[1] 1x on cash/check
[2] 1x on card
[3] 2x on card
[4] 3x or more on card
Option: '''))

if menu == 1:
    new_price = price - (price * 10/100)
    print(f'Your purchase of {price:.2f} will cust {new_price:.2f} in the and')
elif menu == 2:
    new_price = price - (price * 5 / 100)
    print(f'Your purchase of {price:.2f} will cust {new_price:.2f} in the and')
elif menu == 3:
    new_price = price
    installments = new_price / 2
    print(f'Your purchase will be divided into 2x of ${installments:.2f} without interest.')
elif menu == 4:
    payments = int(input('How much payments? '))

    new_price = price + (price * 20/100)
    installments = new_price / payments

    print(f'Your purchase will be divided into {payments}x of ${installments:.2f} with interest.\n'
          f'Your purchase of {price:.2f} will cust {new_price:.2f} in the and')
else:
    print('Invalid option. Please, enter with 1,2,3 or 4')
