term = int(input('How many terms do you want show? '))

a, b = 0, 1

i = 0
while i < term:
    a, b = b, a + b
    i += 1
    print(a, end=' -> ')