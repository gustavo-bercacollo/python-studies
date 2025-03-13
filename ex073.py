from operator import index

fruits = ("apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon",
          "blueberry", "cherry", "mango", "peach", "pear", "kiwi", "papaya", "plum")
print('=' * 180)
print(f'Complete list \033[35m{fruits}\033[m')
print('=' * 180)
print(f'The first 5 numbers are \033[33m{fruits[:6]}\033[m')
print(f'The last 4 numbers are \033[33m{fruits[-4:]}\033[m')
print(f'Fruits in alphabetical order \033[33m{sorted(fruits)}\033[m')
print(f'The kiwi are in {fruits.index('kiwi') + 1}ª position')

#without index using 3 different ways

# 1 way
# position = 0
# for i in fruits:
#     if i == 'kiwi':
#         break
#     position += 1
#
# print(position + 1)

# 2 way
# position = 0
# for i in range(0, len(fruits)):
#     if fruits[i] == 'kiwi':
#         break
#     position += 1
# print(position + 1)

# 3 way
# position = 0
# for pos, i in enumerate(fruits):
#     if i == 'kiwi':
#         break
#     position += 1
# print(position + 1)

