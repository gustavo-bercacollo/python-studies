fruits = (
    'banana', 2.99,
    'apple', 3.50,
    'orange', 2.75,
    'grape', 4.20,
    'watermelon', 7.99,
    'pineapple', 5.50,
    'strawberry', 6.30,
    'blueberry', 8.00,
    'pear', 3.80,
    'mango', 4.50,
    'papaya', 5.00,
    'peach', 4.20,
    'plum', 3.90,
    'cherry', 9.99,
    'kiwi', 4.75
)
print(f'{" SHOPPING LIST ":~^40}')
for i in range(0, len(fruits)):
    if i % 2 == 0:
        print(f'{fruits[i]:.<30}$', end='')
    else:
        print(f'{fruits[i]:>5.2f}')

