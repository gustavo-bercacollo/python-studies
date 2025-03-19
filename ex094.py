data = {'player_name': input('Player name: ')}

matches = int(input(f"How many matches {data['player_name']} played? "))

data['gols'] = []

for i in range(matches):
    gols = int(input(f'How many goals in match {i}? '))
    data['gols'].append(gols)

data['total'] = sum(data['gols'])

print('-=-' * 20)
print(data)
print('-=-' * 20)

for k, v in data.items():
    print(f'The field {k} has the value {v}')

print('-=-' * 20)
print(f"The player {data['player_name']} played {matches} matches.")

for i, gols in enumerate(data['gols']):
    print(f"In match {i}, scored {gols} goals.")

print(f"Total of {data['total']} goals.")
