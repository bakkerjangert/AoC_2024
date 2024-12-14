from collections import defaultdict
from copy import deepcopy
import numpy as np

def show_grid(grd, s):
    print(f'\n---- GRID at second {s} ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

class Robot:
    def __init__(self, x, y, vx, vy, cols, rows):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.cols, self.rows = cols, rows
        self.neighbor = False

    def move(self, s):
        self.x = (self.x + s * self.vx) % self.cols
        self.y = (self.y + s * self.vy) % self.rows

    def get_quadrant(self):
        if self.x < self.cols // 2 and self.y < self.rows // 2:
            return 1
        elif self.cols // 2 < self.x and self.y < self.rows // 2:
            return 2
        elif self.cols // 2 < self.x and self.rows // 2 < self.y:
            return 3
        elif self.x < self.cols // 2 and self.rows // 2 < self.y:
            return 4
        else:
            return 5

    def check_for_neighbor(self, robots):
        for r in robots:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == dy == 0:
                        continue
                    if r.x == self.x + dx and r.y == self.y + dy:
                        self.neighbor, r.neighbor = True, True
                        return

file = 'input.txt'
cols, rows = 101, 103
# file = 'example_01.txt'
# cols, rows = 11, 7

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

quadrants = defaultdict(int)
s = 100
robots = []

for line in data:
    line = line.replace(' v=', ',')
    string = ''.join(char for char in line if char not in ' p=')
    r = Robot(*map(int, string.split(',')), cols, rows)
    robots.append(deepcopy(r))
    r.move(s)
    quadrants[r.get_quadrant()] += 1

answer_pt1 = 1
for q in (1, 2, 3, 4):
    answer_pt1 *= quadrants[q]
print(f'Part 1: {answer_pt1}')

s, ds = 0, 1
search_string = '#' * 8
found = False
while not found:
    s += ds
    grid = np.full((rows, cols), '.')
    for r in robots:
        r.move(ds)
        grid[r.y, r.x] = '#'
    for line in grid:
        string = ''.join(line.tolist())
        if search_string in string:
            print(f'Part 2: {s}')
            show_grid(grid, s)
            found = True
            break
