import numpy as np

def show_grid(grd, tp):
    print(f'\n---- {tp} ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()


keys, locks = list(), list()

for i in range(len(data) // 8 + 1):
    sub_set = data[i * 8: (i + 1) * 8 - 1]
    grid = np.array([list(line.strip()) for line in sub_set])
    mode = 'l' if np.count_nonzero(grid[0] == '#') == 5 else 'k'
    if mode == 'l':
        locks.append(grid)
    if mode == 'k':
        keys.append(grid)

answer_pt1 = 0
for k in keys:
    for l in locks:
        fit = True
        for c in range(5):
            if np.count_nonzero(l[:, c] == '#') + np.count_nonzero(k[:, c] == '#') > 7:
                fit = False
                break
        if fit:
            answer_pt1 += 1
print(f'Part 1: {answer_pt1}')
