# Python Exercise #006 - Double, Triple, Square Root

user_enter = int(input('Enter with a number: '))

print('twice {} is {}.\n'
      'triple {} is {}.\n'
      'the square root of {} is {:.2f}.'
      .format(user_enter, (user_enter * 2), user_enter, (user_enter * 3), user_enter, (user_enter ** 0.5)))