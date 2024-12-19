from collections import Counter, defaultdict
from itertools import combinations, product, permutations

import numpy as np

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')


def can_build_string(target_string, substrings):
    dp = [0] * (len(target_string) + 1)
    dp[0] = 1  # Empty string can be built
    # Check for each position i if the string[:i] can be built up by adding one of the substrings
    # keep counters for possible number of buildups
    for i in range(1, len(target_string) + 1):
        for substring in substrings:
            if i >= len(substring):
                if dp[i - len(substring)] > 0:
                    if target_string[i - len(substring):i] == substring:
                        dp[i] += dp[i - len(substring)]
    return dp[-1]


def add_outerbounds(grid):
    row = np.full(len(grid[0]), '#')
    grid = np.vstack((row, grid, row))
    col = np.full((len(grid), 1), '#')
    grid = np.hstack((col, grid, col))
    return grid


def dijkstra(grid, S, E):
    nodes = np.where(grid == '.')
    nodes = list(zip(nodes[1], nodes[0]))
    links = defaultdict(set)
    for node in nodes:
        x, y = node
        for dx, dy in ((0,1), (0, -1), (1,0), (-1, 0)):
            if grid[y + dy, x + dx] == '.':
                links[(x, y)].add((x + dx, y + dy))
    scores = {n: float('inf') for n in nodes}
    scores[S] = 0
    current_nodes = [S]
    finished_nodes = []
    while len(current_nodes) != 0:
        current_nodes.sort(key=lambda node: scores[node])
        n = current_nodes.pop(0)
        if n == E:
            return scores[n]
        for next_n in links[n]:
            scores[next_n] = min(scores[next_n], scores[n] + 1)
            if next_n not in finished_nodes + current_nodes:
                current_nodes.append(next_n)
        finished_nodes.append(n)
    return None

file = 'example_01.txt'

# Import Grid structure
grid = np.array([list(line.strip()) for line in open(file)])

# Import string
string = open(file, 'r').read()
counted = Counter(open(file, 'r').read())
print(counted)

# Import numbers
int_lists = [[int(num) for num in line.split()] for line in open('numbers.txt')]
print(int_lists)

defdic = defaultdict(int)
for n in [item for sublist in int_lists for item in sublist]:
    defdic[n] += 1
print(defdic)

# Itertools
print('Permutations abc')
for p in permutations(tuple('abc')):
    print(p)

print('Combinations abcdef')
for c in combinations(tuple('abcdef'), 2):
    print(c)