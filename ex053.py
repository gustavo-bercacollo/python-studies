# Python Exercise #053 - Palindrome Detector

phrase = str(input('Enter with any phrase: ')).replace(' ', '')

inverse = ''
for i in range(len(phrase) -1, -1, -1):
    inverse += phrase[i]

print(f'The inverse of {phrase} is {inverse} ')

if phrase == inverse:
    print('The enter frase is a palindrome')
else:
    print('The enter frase is not a palindrome')


