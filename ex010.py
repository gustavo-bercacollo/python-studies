# Python Exercise #010 - Currency Converter to R$

amount = float(input('How much money do you have in your wallet? $'))

print('With ${:.2f} you can buy R${:.2f}'.format(amount, (amount * 5.75)))
