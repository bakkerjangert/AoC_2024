import numpy as np

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

id, j = 0, 0
for _, line in enumerate(data):
    id = id + 1 if '#' in line else id
    if len(line) > 0:
        if line[0] in '<>^v' and j == 0:
            j = _

grid = np.array([list(line.strip()) for line in data[0:id]])
instructions = ''.join(data[j:])
pos = np.where(grid == '@')
x, y = pos[1][0], pos[0][0]
grid[y, x] = '.'

for i in instructions:
    sub_grid, dx, dy = None, None, None
    if i == '<':
        sub_grid = grid[y, 0:x][::-1]
        dx, dy = -1, 0
    elif i == '>':
        sub_grid = grid[y, x + 1:]
        dx, dy = 1, 0
    elif i == '^':
        sub_grid = grid[0:y, x][::-1]
        dx, dy = 0, -1
    elif i == 'v':
        sub_grid = grid[y + 1:, x]
        dx, dy = 0, 1
    if '.' in sub_grid:
        if sub_grid[0] == 'O':
            point, wall = np.where(sub_grid == '.')[0][0], np.where(sub_grid == '#')[0][0]
            if point < wall:
                sub_grid[np.where(sub_grid == '.')[0][0]] = 'O'
                sub_grid[0] = '.'
        if sub_grid[0] == '.':
            x += dx
            y += dy
# grid[y, x] = '@'
# show_grid(grid)
# grid[y, x] = '.'
answer_pt1 = 0
ys, xs = np.where(grid == 'O')
for x, y in zip(xs, ys):
    answer_pt1 += x + 100 * y
print(f'Part 1: {answer_pt1}')

grid = np.array([list(line.strip()) for line in data[0:id]])
grid = grid.transpose()
doubled_grid = grid.copy()
i = 1
for row in grid:
    new_row = row.copy()
    for _ in np.where(row == 'O')[0]:
        row[_] = '['
        new_row[_] = ']'
    if '@' in new_row:
        new_row[np.where(row == '@')[0]] = '.'
    doubled_grid[i - 1] = row.copy()
    doubled_grid = np.insert(doubled_grid, i, new_row.copy(), axis=0)
    i += 2
doubled_grid = doubled_grid.transpose()
# show_grid(doubled_grid)
pos = np.where(doubled_grid == '@')
x, y = pos[1][0], pos[0][0]
doubled_grid[y, x] = '.'
for i in instructions:
    sub_grid, dx, dy = None, None, None
    if i == '<':
        sub_grid = doubled_grid[y, 0:x][::-1]
        dx, dy = -1, 0
    elif i == '>':
        sub_grid = doubled_grid[y, x + 1:]
        dx, dy = 1, 0
    elif i == '^':
        sub_grid = doubled_grid[0:y, x][::-1]
        dx, dy = 0, -1
    elif i == 'v':
        sub_grid = doubled_grid[y + 1:, x]
        dx, dy = 0, 1
    if '.' in sub_grid:
        if sub_grid[0] in '[]':
            # First horizontal push
            if i in '<>':
                point, wall = np.where(sub_grid == '.')[0][0], np.where(sub_grid == '#')[0][0]
                if point < wall:
                    sub_grid[1: point + 1] = sub_grid[: point].copy()
                    sub_grid[0] = '.'
            # vertical push
            elif i in '^v':
                bx, by = x + dx, y + dy
                box = (bx, bx + 1, by) if doubled_grid[by, bx] == '[' else (bx - 1, bx, by)
                boxes = [set()]
                boxes[-1].add(box)
                pushable = True
                cur_y = by
                while len(boxes[-1]) != 0 and pushable:
                    boxes.append(set())
                    cur_y += dy
                    for box in boxes[-2]:
                        for cur_x in box[:-1]:
                            if doubled_grid[cur_y, cur_x] == '#':
                                pushable = False
                            elif doubled_grid[cur_y, cur_x] == '[':
                                new_box = (cur_x, cur_x + 1,cur_y)
                                boxes[-1].add(new_box)
                            elif doubled_grid[cur_y, cur_x] == ']':
                                new_box = (cur_x - 1, cur_x, cur_y)
                                boxes[-1].add(new_box)
                if pushable:
                    for boxs in boxes[::-1]:  # Start at outer row to prevent overlaps
                        for box in boxs:
                            for cx in box[:-1]:
                                doubled_grid[box[2] + dy, cx] = doubled_grid[box[2], cx]
                                doubled_grid[box[2], cx] = '.'
        if sub_grid[0] == '.':
            x += dx
            y += dy
doubled_grid[y, x] = '@'
show_grid(doubled_grid)
answer_pt2 = 0
ys, xs = np.where(doubled_grid == '[')
for x, y in zip(xs, ys):
    answer_pt2 += x + 100 * y
print(f'Part 2: {answer_pt2}')
