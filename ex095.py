# Python Exercise #095 - Improving Dictionaries

players = []

while True:
    data = {'player_name': input('Player name: ')}
    matches = int(input(f"How many matches {data['player_name']} played? "))
    data['gols'] = []

    for i in range(matches):
        gols = int(input(f'How many goals in match {i+1}? '))
        data['gols'].append(gols)

    data['total'] = sum(data['gols'])

    players.append(data.copy())
    advance = ' '
    while advance not in 'YN':
        advance = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if advance == 'N':
        break
print('—' * 30)
print(f'{"cod":<5}{"name":<10}{"gols":<10}{"total":<10}')
for k, v in enumerate(players):
    print(f'{k:<5}{v["player_name"]:<10}{str(v["gols"]):<10}{v["total"]:<10}')

while True:
    more_about_players = int(input('Show data about what player? (999 to cancel) '))
    if more_about_players == 999:
        break
    if 0 <= more_about_players < len(players):
        print(f'DATA ABOUT THE PLAYER {players[more_about_players]["player_name"]}:')
        for i, v in enumerate(players[more_about_players]['gols']):
            print(f'In the game {i+1} make {v} gols')
    else:
        print(f'Player {more_about_players} do not exist. Try again!')

print('Bye!')