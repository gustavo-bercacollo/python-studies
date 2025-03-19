# Python Exercise #096 - Function that calculates area

def area(width, height):
    total_area = width * height
    print(f'The area of a land {width}x{height} is {total_area}m²')


print('land control')
print('—' * 15)
width = float(input('Width (m): '))
height = float(input('Height (m): '))

area(width, height)