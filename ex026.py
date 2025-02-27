# Exercise Python #026 - First and Last Occurrence of a String

user_enter = str(input('Enter with a phrase: ')).lower().replace(' ', '').strip()

letter_count = user_enter.count('a')
find_firth_a = user_enter.find('a') + 1
find_Last_a = user_enter.rfind('a') + 1

print(
    f'''
    The letter 'a' appears {letter_count} in the phrase.
    The firth letter 'a' appeared in the position {find_firth_a}
    The last letter 'a' appeared in the position {find_Last_a}
    ''')