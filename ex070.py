print(f'{'STORE':—^30}')

total = thousand = counter = lowest_value = 0
lowest_value_product = ' '

while True:
    product = str(input('Product name: '))
    price = float(input('Price: $'))
    total += price
    counter += 1
    advance = ' '
    while advance not in 'SN':
        advance = str(input('Do you want continue? ')).strip().upper()[0]

    if price > 1000:
        thousand += 1
    if counter == 1 or price < lowest_value:
        lowest_value = price
        lowest_value_product = product
    if advance == 'N':
        break
print(f'The total purchase was {total:.2f}')
print(f'We have {thousand} product that cost more $1000' if thousand == 1 else print(f'We have {thousand} products that cost more $1000'))
print(f'The cheapest product was {lowest_value_product} that cost {lowest_value:2.f}')