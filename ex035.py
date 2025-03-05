# Python Exercise #035 - Analyzing Triangle v1.0

print('-=-=-=-=-=-=-=-=-=-\n'
      'Triangle Analyzed\n'
      '-=-=-=-=-=-=-=-=-=-')

side_a = float(input('First segment: '))
side_b = float(input('Second segment: '))
side_c = float(input('Third segment: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
      print('The segments can become a triangle')
else:
      print('The segments cannot become a triangle')