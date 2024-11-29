import numpy as np
from copy import deepcopy
import random

file = 'input.txt'
# file = 'example 02.txt'

class Star:
    def __init__(self, name, x, y):
        self.name = name
        self.x, self.y = x, y
        self.neighbors = []

    def __eq__(self, other):
        return isinstance(other, Star) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.name, self.x, self.y))

    def __repr__(self):
        return f'Star "{self.name}" at ({self.x}, {self.y})'


class Connection:
    def __init__(self,name, s1, s2):
        """
        :param name: string
        :param s1: Star 1, always use the upper left star
        :param s2: Star 2, always use the lower right star
        """
        self.name = name
        self.s1, self.s2 = s1, s2
        self.horizontal = True if self.s1.y == self.s2.y else False
        self.vertical = True if self.s1.x == self.s2.x else False
        self.connections = set()
        self.intersects = set()

    def Intersect(self, other):
        if (self.horizontal and other.horizontal) or (self.vertical and other.vertical):
            return False
        if self.horizontal:
            if self.s1.x < other.s1.x < self.s2.x:
                if other.s1.y < self.s1.y < other.s2.y:
                    return True
                else:
                    return False
            else:
                return False
        elif self.vertical:
            if self.s1.y < other.s1.y < self.s2.y:
                if other.s1.x < self.s1.x < other.s2.x:
                    return True
                else:
                    return False
            else:
                return False
        else:
            print('Warning: Connection not vertical or horizontal, check input!')
            return None

    def __eq__(self, other):
        return isinstance(other, Connection) and self.s1 == other.s1 and self.s2 == other.s2

    def __hash__(self):
        return hash((self.name, self.s1, self.s2))

    def __repr__(self):
        return f'Connection from Star {self.s1} to {self.s2}, a {"horizontal" if self.horizontal else "vertical"} connection'


def show_grid(grid):
    for line in grid:
        for char in line:
            if char == '*':
                print(f'\033[33m{char}\033[0m', end='')
            elif char in '-|+':
                print(f'\033[31m{char}\033[0m', end='')
            else:
                print(f'{char}', end='')
        print('')
    print('\n------\n')

with open(file, 'r') as f:
    data = f.read().splitlines()

stars, n = [], 0
grid = np.empty((len(data), len(data[0])), dtype=str)
grid.fill('.')

# Setup Stars
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == '*':
            grid[y, x] = '*'
            stars.append(Star(n, x, y))
            # Add left / right neighbors
            if n > 0:
                if stars[n - 1].y == y:
                    stars[n].neighbors.append(n - 1)
                    stars[n - 1].neighbors.append(n)
            # Add upper / lower neighbor
            if n > 0:
                for star in stars[:n][::-1]:
                    if star.x == x:
                        stars[star.name].neighbors.append(n)
                        stars[n].neighbors.append(star.name)
                        break
            n += 1

# Setup Connections
connections = []
name = 0
for i, star in enumerate(stars):
    for neighbor in star.neighbors:
        if star.name < neighbor:
            connections.append(Connection(name, star, stars[neighbor]))
            name += 1

# Add neighbors and intersections to the connections
for i, c1 in enumerate(connections[:-1]):
    for j , c2 in enumerate(connections[i + 1:]):
        if c1.s1 in (c2.s1, c2.s2) or c1.s2 in (c2.s1, c2.s2):
            print(f'Connection found: {c1} <-> {c2}')
            c1.connections.add(c2), c2.connections.add(c1)
        elif c1.Intersect(c2):
            print(f'Crossed connection found: {c1} --> {c2}')
            c1.intersects.add(c2), c2.intersects.add(c1)

for star in stars:
    grid[star.y, star.x] = '*'

stars_min, stars_max = 3, 10
signs = set()

for i, c in enumerate(connections):
    print(f'Analyzing {i + 1} from {len(connections)}')
    print(len(signs))
    current_signs = set()
    current_signs.add((c.name,))
    while len(current_signs) > 0:
        current_sign = current_signs.pop()
        stars = set(sorted([connections[c_1].s1.name for c_1 in current_sign] + [connections[c_2].s2.name for c_2 in current_sign]))
        if current_sign in signs:
            # sign already evaluated
            continue
        if stars_min <= len(stars) <= stars_max:
            # s = [con for con in current_sign]
            # print(s)
            signs.add(tuple(sorted(current_sign))) # Sort to make sure set does not find similar signs with different order
        if len(stars) <= stars_max:
            neighbors = []
            for c_3 in current_sign:
                for neighbor in connections[c_3].connections:
                    if neighbor.name not in current_sign:
                        crossed = False
                        for c_4 in current_sign:
                            if neighbor in connections[c_4].intersects:
                                crossed = True
                        if not crossed:
                            neighbors.append(neighbor.name)
            for neighbor_ in neighbors:
                current_signs.add(tuple(sorted(current_sign + (neighbor_,))))

print(len(signs))

signs_to_be_printed = 10
tup_signs = tuple(signs)

for _ in range(signs_to_be_printed):
    subgrid = grid.copy()
    sign = random.choice(tup_signs)
    for c in sign:
        con = connections[c]
        if con.horizontal:
            subgrid[con.s1.y, con.s1.x + 1: con.s2.x] = '-'
        elif con.vertical:
            subgrid[con.s1.y + 1: con.s2.y, con.s1.x] = '|'
    show_grid(subgrid)