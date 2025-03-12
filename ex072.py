# Python Exercise #072 - Number in Words

numbers_in_words = (
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
)

num = -1
while num not in range(21):
    num = int(input('Enter with a number between 0 and 20: '))
    while not (0 <= num <= 20):
        num = int(input('Try again. Enter with a number between 0 and 20: '))

    print(f'You entered the number {numbers_in_words[num]}')
    advance = str(input('Do you want continue? [S/N]: ')).strip().upper()[0]

    if advance == 'N':
        break
    num  = -1