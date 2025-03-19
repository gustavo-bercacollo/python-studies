# Python Exercise #097 - A special print

def write(message):
    print('~' * (len(message) + 4))
    print(f'  {message}  ')
    print('~' * (len(message) + 4))


write(input('Enter your message: '))
