import numpy as np
from collections import defaultdict

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

def add_outerbounds(grid):
    row = np.full(len(grid[0]), 'O')
    grid = np.vstack((row, grid, row))
    col = np.full((len(grid), 1), 'O')
    grid = np.hstack((col, grid, col))
    return grid

file = 'input.txt'
# file = 'example_01.txt.txt'

grid = np.array([list(line.strip()) for line in open(file)])
grid = add_outerbounds(grid)
pos = (int(np.where(grid == 'S')[1][0]), int(np.where(grid == 'S')[0][0]),)
path = [pos,]

while True:
    x, y = path[-1]
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if grid[y + dy, x + dx] in '.E' and (x + dx, y + dy) not in path:
            path.append((x + dx, y + dy,))
    if grid[y, x] == 'E':
        break

grid[path[0][1], path[0][0]] = '.'
grid[path[-1][1], path[-1][0]] = '.'

saves = defaultdict(int)
walls = np.where(grid == '#')
walls = list(zip(walls[1], walls[0]))

answer_pt1 = 0
for wall in walls:
    x, y = wall
    p1, p2 = None, None
    if grid[y + 1, x] == '.' and grid[y - 1, x] == '.':
        p1, p2 = (x, y + 1), (x, y - 1)
    elif grid[y, x + 1] == '.' and grid[y, x - 1] == '.':
        p1, p2 = (x + 1, y), (x - 1, y)
    if p1 is not None:
        i1, i2 = sorted((path.index(p1), path.index(p2)))
        saves[i2 - i1 - 1 - 1] += 1
        if i2 - i1 - 1 - 1 >= 100:
            answer_pt1 += 1
print(f'Part 1: {answer_pt1}')

saves = defaultdict(int)
delta = 100
# delta = 50
for i, p1 in enumerate(path[:-1 - delta]):
    x1, y1 = p1
    for j, p2 in enumerate(path[i + delta:]):
        x2, y2 = p2
        if abs(x1 - x2) + abs(y1 - y2) <= 20:
            saves[j + delta - abs(x1 - x2) - abs(y1 - y2)] += 1
keys = sorted(saves.keys())
keys = [k for k in keys if k >= delta]
print(f'Part 2: {sum([saves[k] for k in keys])}')
