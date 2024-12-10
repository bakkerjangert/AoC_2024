import numpy as np

def show_grid(grid):
    print('\n---- GRID ----\n')
    for line in grid:
        for char in line:
            print(char, end='')
        print('')

SHOW_GRID = True
file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

x_max, y_max = len(data[0]), len(data)
nodes = dict()
for y in range(y_max):
    for x in range(x_max):
        if data[y][x] != '.':
            char = data[y][x]
            if char not in nodes:
                nodes[char] = [(x, y)]
            else:
                nodes[char].append((x, y))

antinodes_pt1, antinodes_pt2 = set(), set()
for mark in nodes:
    for i, n1 in enumerate(nodes[mark][:-1]):
        for n2 in nodes[mark][i + 1:]:
            antinodes_pt2.add(n1), antinodes_pt2.add(n2)
            dx, dy = n2[0] - n1[0], n2[1] - n1[1]
            # backwards
            x, y = n1[0] - dx, n1[1] - dy
            if 0 <= x < x_max and 0 <= y < y_max:
                antinodes_pt1.add((x, y))
            while 0 <= x < x_max and 0 <= y < y_max:
                antinodes_pt2.add((x, y))
                x, y = x - dx, y - dy
            # forward
            x, y = n2[0] + dx, n2[1] + dy
            if 0 <= x < x_max and 0 <= y < y_max:
                antinodes_pt1.add((x, y))
            while 0 <= x < x_max and 0 <= y < y_max:
                antinodes_pt2.add((x, y))
                x, y = x + dx, y + dy
print(f'Part 1: {len(antinodes_pt1)}')
print(f'Part 2: {len(antinodes_pt2)}')

if SHOW_GRID:
    grid = np.full((y_max, x_max), '.', dtype=str)
    for char in nodes:
        for pos in nodes[char]:
            grid[pos[1], pos[0]] = char
    show_grid(grid)
    for pos in antinodes_pt1:
        grid[pos[1], pos[0]] = '#'
    show_grid(grid)
    for pos in antinodes_pt2:
        grid[pos[1], pos[0]] = '#'
    show_grid(grid)

