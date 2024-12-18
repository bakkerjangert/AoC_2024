from collections import defaultdict

import numpy as np

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

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

file = 'input.txt'
r, c = 71, 71
b = 1024
# file = 'example_01.txt'
# r, c = 7, 7
# b = 12

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

S, E = (1, 1), (c, r)  # due to adding boundaries to prevent out of bound

bites = defaultdict(tuple)
for i in range(len(data)):
    bites[i] = tuple(map(int, data[i].split(',')))

grid = np.full((r, c), '.')
for i in range(b):
    x, y = bites[i]
    grid[y, x] = '#'

grid = add_outerbounds(grid)
print(f'Part 1: {dijkstra(grid, S, E)}')

low, high = b, len(bites)
b = low + (high - low) // 2
while True:
    grid = np.full((r, c), '.')
    for i in range(b - 1):
        x, y = bites[i]
        grid[y, x] = '#'
    grid = add_outerbounds(grid)
    if dijkstra(grid, S, E) is None:  # guess to high
        # print('Guess to high!')
        high = b
        b = low + (high - low) // 2
        continue
    x, y = bites[b - 1]
    grid[y + 1, x + 1] = '#'  # boundaries already added!
    if dijkstra(grid, S, E) is not None:  # guess is to low
        # print('Guess to low!')
        low = b
        b = low + (high - low) // 2
        continue
    print(f'Part 2: {bites[b - 1][0]},{bites[b - 1][1]}')
    break
