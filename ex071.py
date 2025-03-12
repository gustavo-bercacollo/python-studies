#Python Exercise #071 - ATM Simulator

value = int(input('Amount to withdraw: $'))


banknote100 = banknote50 = banknote20 = banknote10 = banknote5 = banknote2 = 0

while value > 0:
    if value >= 100:
        value -= 100
        banknote100 += 1
    elif value >= 50:
        value -= 50
        banknote50 += 1
    elif value >= 20:
        value -= 20
        banknote20 += 1
    elif value >= 10:
        value -= 10
        banknote10 += 1
    elif value >= 5:
        value -= 5
        banknote5 += 1
    elif value >= 2:
        value -= 2
        banknote2 += 1
    else:
        break

if banknote100 > 0:
    print(f"Banknotes of 100: {banknote100}")
if banknote50 > 0:
    print(f"Banknotes of 50: {banknote50}")
if banknote20 > 0:
    print(f"Banknotes of 20: {banknote20}")
if banknote10 > 0:
    print(f"Banknotes of 10: {banknote10}")
if banknote5 > 0:
    print(f"Banknotes of 5: {banknote5}")
if banknote2 > 0:
    print(f"Banknotes of 2: {banknote2}")
