# Python Exercise #012 - Calculating Discounts

price = float(input("What's product price? $"))
discount = price - (price * (5 / 100))

print('The product witch costed ${:.2f}, in promotion with discount of 5% will cost ${:.2f}'
      .format(price, discount))