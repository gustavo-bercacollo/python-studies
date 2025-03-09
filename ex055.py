# Python Exercise #055 - Largest and smallest of the sequence

largest_weight = 0
smallest_weight = 0

for i in range(1, 6):
    weight = float(input(f'Weight of person {i}: '))
    if i == 1:
        largest_weight = weight
        smallest_weight = weight
    else:
        if weight > largest_weight:
            largest_weight = weight
        if weight < smallest_weight:
            smallest_weight = weight

print(f'Largest weight: {largest_weight} kg')
print(f'smallest weight: {smallest_weight} kg')