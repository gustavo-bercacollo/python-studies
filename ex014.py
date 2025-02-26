# Python Exercise #014 - Temperature Converter

celsius = float(input('Report the temperature: '))
fahrenheit = (celsius * 9/5) + 32

print('The temperature of {:.2f}°C correspond to {:.2f}°F'
      .format(celsius, fahrenheit))