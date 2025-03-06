# Python Exercise #038 - Comparing Numbers

try:
    first_number = int(input('First number: '))
    second_number = int(input('First number: '))

    if first_number > second_number:
        print('The first number is greater then second')
    elif first_number < second_number:
        print('The second number is greater then first')
    else:
        print('The first number is equal to second number')

except ValueError:
    print("Error: Please, enter with only integer numbers!")
