# Python Exercise #042 - Analyzing Triangles v2.0

print('-=-=-=-=-=-=-=-=-=-\n'
      'Triangle Analyzed\n'
      '-=-=-=-=-=-=-=-=-=-')

side_a = float(input('First segment: '))
side_b = float(input('Second segment: '))
side_c = float(input('Third segment: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print('The segments can form a triangle ', end='')

    if side_a == side_b == side_c:
        print('equilateral.')
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print('isosceles.')
    else:
        print('scalene.')
else:
    print('The segments cannot form a triangle.')
