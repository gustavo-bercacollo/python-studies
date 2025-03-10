# Python Exercise #064 - Handling Multiple Values v1.0

num = total = counter = 0
while True:
    num = int(input('Enter with a number [999 to stop]: '))
    if num == 999:
        break
    else:
     total += num
     counter += 1
print(f'You entered with {counter} numbers and their sum is {total}')
