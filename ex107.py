# Python Course #22 - Modules and Packages

from utils import coin

enter_user = float(input('Enter the price: $'))
print(f'The half of {enter_user} is {coin.half_price(enter_user):.2f}')
print(f'The double of {enter_user} is {coin.double_price(enter_user):.2f}')
print(f'Increasing 10% of {enter_user} we have {coin.increase_ten_percent(enter_user)}')
print(f'Decreasing 13% of {enter_user} we have {coin.decreases_thirteen_percent(enter_user)}')





