# Python Exercise #065 - Largest and Smallest Values

# with append
counter = 0
total = []

while True:
    num = int(input('Enter with a number: '))
    user_response = str(input('Do you want to continue? [s/n]')).lower().strip()[0]
    counter += 1
    total.append(num)
    if user_response == 'n':
        break

print(f'You enter with {counter} numbers and the average was {sum(total)/len(total):.1f}')
print(f'The largest value was {max(total)} and lowest was {min(total)}')

#without append

# total = counter = 0
# largest = lowest = 0
# while True:
#     num = int(input('Enter with a number: '))
#     user_response = str(input('Do you wanna continue? [s/n]')).lower().strip()[0]
#     counter += 1
#     total += num
# 
# 
#     if counter == 1:
#         largest = lowest = num
#     else:
#         if num > largest:
#             largest = num
#         if num < lowest:
#             lowest = num
#     if user_response == 'n':
#         break
# 
# print(f'You enter with {counter} numbers and the average was {total/counter:.1f}')
# print(f'The largest value was {largest} and lowest was {lowest}')