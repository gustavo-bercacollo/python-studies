# Create a program that reads something from the keyboard and displays its primitive type and all possible information about it.

user_enter = input('Type something: ')
what_type = type(user_enter)
contains_space = user_enter.isspace()
is_a_number = user_enter.isnumeric()
is_alphabetical = user_enter.isalpha()
is_alphanumeric = user_enter.isalnum()
is_upper = user_enter.isupper()
is_lower = user_enter.islower()
is_capitalized = user_enter.istitle()

print(
    'the primitive type is {} \n'
    'just have spaces? {} \n'
    'is a number? {} \n'
    'is alphabetical? {} \n'
    'is alphanumeric? {} \n'
    'is uppercase? {} \n'
    'is lowercase? {} \n'
    'is capitalized? {} \n'.format(what_type, contains_space, is_a_number, is_alphabetical, is_alphanumeric, is_upper, is_lower, is_capitalized)
    )