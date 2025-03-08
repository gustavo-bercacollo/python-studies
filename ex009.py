# multiplication table
# improved version in the exercise 049
user_enter = int(input('Enter with a number to see your multiplication table: '))

print(
'____________\n'
'{} x  1 = {}\n'
'{} x  2 = {}\n'
'{} x  3 = {}\n'
'{} x  4 = {}\n'
'{} x  5 = {}\n'
'{} x  6 = {}\n'
'{} x  7 = {}\n'
'{} x  8 = {}\n'
'{} x  9 = {}\n'
'{} x 10 = {}\n'
'____________'
.format(
user_enter, (user_enter * 1),
user_enter, (user_enter * 2),
user_enter, (user_enter * 3),
user_enter, (user_enter * 4),
user_enter, (user_enter * 5),
user_enter, (user_enter * 6),
user_enter, (user_enter * 7),
user_enter, (user_enter * 8),
user_enter, (user_enter * 9),
user_enter, (user_enter * 10)
))


