import numpy as np
from collections import deque

def show_grid(grid):
    print('\n---- GRID ----\n')
    for line in grid:
        for char in line:
            print(char, end='')
        print('')

def walk(grid, guard, pos, d, pt1=False):
    blocks = set()
    while True:
        path, i, f = None, 0, 0
        if guard == '^':
            path = grid[:pos[0] + 1, pos[1]][::-1]
            i, f = 0, -1
        elif guard == '>':
            path = grid[pos[0], pos[1]:]
            i, f = 1, 1
        elif guard == 'v':
            path = grid[pos[0]:, pos[1]]
            i, f = 0, 1
        elif guard == '<':
            path = grid[pos[0], :pos[1] + 1][::-1]
            i, f = 1, -1
        n = np.where(path == '#')
        if len(n[0]) == 0:  # Walking out of grid
            path[:] = 'X'
            return 0 if not pt1 else np.where(grid == 'X')
        n = n[0][0]  # Index of first block
        path[:n] = 'X'
        block = pos[:]
        block[i] += n * f
        block.append(guard)
        if tuple(block) in blocks:  # Previous block with same guard direction found --> Loop
            if pt1:
                print('Huh? Why here?')
            return 1
        blocks.add(tuple(block))
        pos[i] += (n - 1) * f
        d.rotate(-1)
        guard = d[0]

file = 'input.txt'
# file = 'example_01.txt.txt'
file = 'aoc-2024-day-06-challenge-3.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

grid = np.empty((len(data), len(data[0])), dtype='str')

for y, line in enumerate(data):
    for x, char in enumerate(line):
        grid[y, x] = char

d = deque(('^', '>', 'v', '<'))
pos, guard = None, None

for g in d.copy():
    if np.any(grid == g):
        pos, guard = np.where(grid == g), g
        pos = [pos[0][0], pos[1][0]]
        d.rotate(d.index(guard))

visited_positions = walk(grid.copy(), guard, pos[:], d.copy(), pt1=True)
answer_pt1 = len(visited_positions[0])
print(f'Part 1: {answer_pt1}')

answer_pt2 = 0
for y, x in zip(visited_positions[0], visited_positions[1]):
    new_grid = grid.copy()
    new_grid[y, x] = '#'
    answer_pt2 += walk(new_grid, guard, pos[:], d.copy())
print(f'Part 2: {answer_pt2}')
