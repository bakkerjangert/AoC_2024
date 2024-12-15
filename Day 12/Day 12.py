import numpy as np

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

file = 'input.txt'
# file = 'example_01.txt'
# file = 'example_02.txt.txt'

grid = np.array([list(line.strip()) for line in open(file)])
x_max, y_max = len(grid[0]), len(grid)

sides = {(0, 1): 'v', (0, -1): '^', (1, 0): '>', (-1, 0): '<'}
answer_pt1, answer_pt2 = 0, 0
for y, line in enumerate(grid):
    while np.count_nonzero(line == '#') != len(line):
        # show_grid(grid)
        boundaries = []
        x = np.argmax(line != '#')
        char = grid[y, x]
        positions = [(x, y)]
        current_area = [(x, y)]
        while len(positions) > 0:
            cur_x, cur_y = positions.pop(0)
            grid[cur_y, cur_x] = '#'
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                next_x, next_y = cur_x + dx, cur_y + dy
                side = sides[(dx, dy)]
                if not 0 <= next_x < x_max or not 0 <= next_y < y_max:  # out of grid
                    boundaries.append((cur_x, cur_y, side))
                elif grid[next_y, next_x] != char and (next_x, next_y) not in current_area:
                    boundaries.append((cur_x, cur_y, side))
                elif grid[next_y, next_x] == char and (next_x, next_y) not in current_area:
                    positions.append((next_x, next_y))
                    current_area.append((next_x, next_y))
        answer_pt1 += len(current_area) * len(boundaries)
        double_edges = []
        for d in ('^', '<', '>', 'v'):
            bounds = [n for n in boundaries if n[2] == d]
            if d in '<>':
                sorted_boundaries = sorted(bounds, key=lambda x: (x[0], x[1]))
                a, b = (0, 1)
            elif d in '^v':
                sorted_boundaries = sorted(bounds, key=lambda x: (x[1], x[0]))
                a, b = (1, 0)
            for b1, b2 in zip(sorted_boundaries[:-1], sorted_boundaries[1:]):
                if b1[0] + a == b2[0] and b1[1] + b == b2[1]:
                    double_edges.append(boundaries.index(b2))
        answer_pt2 += (len(boundaries) - len(double_edges)) * len(current_area)
        # print(f'added {len(current_area)} x {len(boundaries)} with mar {char}')
        # print(f'Adding {len(current_area)} x {boundary}')
print(f'Part 1: {answer_pt1}')
print(f'Part 2: {answer_pt2}')
