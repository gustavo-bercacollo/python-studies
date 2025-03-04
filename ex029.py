# Python Exercise #029 - Electronic Speed Radar

speed = float(input('What is the current speed of the car? ').strip())
fine = (speed - 80) * 7

if speed > 80:
    print('\033[1;31mFINED!\033[m \033[31mYou exceeded the safety limit of 80km/h and\n'
          f'You must pay a fine of ${fine:.2f}\033[m')

print('\033[33mHave a good day, drive safely!')