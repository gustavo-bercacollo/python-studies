from random import randint
from time import sleep
from operator import itemgetter

players = {
    'player1': randint(1, 6),
    'player2': randint(1, 6),
    'player3': randint(1, 6),
    'player4': randint(1, 6),
}

for k, v in players.items():
    print(f'The {k} played {v}')
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('—' * 20)
print('RANKING')
for i, v in enumerate(ranking):
    print(f'The {i+1}º place: {v[0]} with {v[1]} ')
    sleep(1)


