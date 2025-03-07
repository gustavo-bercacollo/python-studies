# Python Exercise #043 - Body Mass Index

weight = float(input('What is your weight? (Kg) '))
height = float(input('What is your height? (m) '))

imc = weight / (height ** 2)

print(f'Your IMC is {imc:.1f} and you are ', end='')
if imc < 18.5:
    print('underweight')
elif 18.5 <= imc < 25:
    print('ideal weight')
elif 25 <= imc < 30:
    print('overweight')
elif 30 <= imc < 40:
    print('obesity')
else:
    print('morbid obesity')