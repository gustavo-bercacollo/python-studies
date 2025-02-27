# Exercise Python #024 - Checking the First Words of a Text

user_enter = str(input('What city were you born in? ')).strip().lower()

split_phase = user_enter.split()[0]
check_word = 'santo' in split_phase

print(check_word)
