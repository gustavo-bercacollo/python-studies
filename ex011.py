# Python Exercise #011 - Painting the Wall

width_wall = float(input('Wall width: '))
height_wall = float(input('Height wall: '))
area = width_wall * height_wall

print('The wall has dimensions of {}x{} and its area is {}m²\n'
      'to paint this wall, you will need {}l of ink'
      .format(width_wall, height_wall, area, (area / 2) ))