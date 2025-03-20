# Python Exercise #103 - Player Sheet

def player_sheet(player = '<Unknown>', gols = 0):
    print(f'The player {player} score {gols} in the championship')


player_name = input("Player's name: ").strip()
num_of_gols = input('Numbers of gols: ')

if player_name == '':
    player_name = '<Unknown>'
if num_of_gols.isdigit():
    num_of_gols = int(num_of_gols)
else:
    num_of_gols = 0

player_sheet(player_name, num_of_gols)