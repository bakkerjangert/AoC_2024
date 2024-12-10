import random

from numpy.ma.core import swapaxes


class MontyHall:
    def __init__(self, switch=True, doors=tuple('ABC')):
        self.switch = switch
        self.doors = doors
        self.simulation_results = {'games': [], 'wins': [], 'ratios':[]}

    def simulate(self,n):
        games, wins, ratio = n, 0, 0
        for game in range(games):
            player_choice, winning_door = random.choice(self.doors), random.choice(self.doors)
            if player_choice != winning_door and self.switch:
                wins += 1
            if player_choice == winning_door and not self.switch:
                wins += 1
        self.simulation_results['games'].append(games)
        self.simulation_results['wins'].append(wins)
        self.simulation_results['ratios'].append(wins / games)

def play(n, switch=True):
    if n > 26:
        print('Warning: Maximum 26 doors allowed!')
    doors = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:n]
    prize = random.choice(doors)
    player_choice = random.choice(doors)
    remaining_doors = doors[:]
    remaining_doors.remove(player_choice)
    remaining_door = prize if player_choice != prize else random.choice(remaining_doors)
    if switch:
        player_choice = remaining_door
    return True if player_choice == prize else False

games, number_of_doors, wins = 10000, 3, 0
for game in range(games):
    if play(number_of_doors, switch=False):
        wins += 1

print(f'Wins = {wins} of {games} = {wins / games * 100:.1f}%')