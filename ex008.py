# Python Exercise #008 - Measurement Converter

user_enter = int(input('Enter with a distance in meters: '))

print('The measurement of {}m corresponds to\n'
      '{}km\n'
      '{}hm\n'
      '{}dam\n'
      '{}dm\n'
      '{}cm\n'
      '{}mm'
      .format
      (user_enter,
      (user_enter / 1000),
      (user_enter / 100),
      (user_enter / 10),
      (user_enter * 10),
      (user_enter * 100),
      (user_enter * 1000)))