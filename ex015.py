# Python Exercise #015 - Car Rental

days_rented = int(input('How many days rented? '))
km_driven = int(input('How many km driven? '))
total = days_rented * 60 + km_driven * 0.15

print('The total to be paid is {:.2f}'.format(total))