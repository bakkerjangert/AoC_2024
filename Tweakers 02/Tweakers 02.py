from collections import deque
import numpy as np

def decode(n1, n2, data):
    # Only works for square input data with even number of rows / columns!
    # Extract strings per perimeter, starting at outer boundary, working inwards
    # Shift with deque and add to final np array
    # For part 1 extract pos 0 and pos half string length
    l = len(data[0])
    s1, s2 = '', ''
    for i in range(l // 2):
        # Top row left to right
        string = data[i][i: l - i]
        # Right col top to bottom
        for j in range(i + 1, l - i - 1):
            string += data[j][l - i - 1]
        # bottom row right to left
        string += data[l - i - 1][i: l - i][::-1]
        # left col bottom to up
        for k in range(l - i - 2, i, -1):
            string += data[k][i]
        dq = deque(list(string))
        dq.rotate(-n1)
        s1 += dq[0]
        s2 += dq[len(dq) // 2]
        dq.rotate(n1)
        dq.rotate(-n2)
        # Put in grid
        x, y = i, i
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n_min, n_max = i, i + (len(dq) + 4) // 4 - 1
        dir_index = 0
        for char in dq:
            grid[y, x] = char
            x, y = x + directions[dir_index][0], y + directions[dir_index][1]
            if (x, y) == (n_max, n_min) or (x, y) == (n_max, n_max) or (x, y) == (n_min, n_max):
                dir_index += 1
    print(f'Part 1: {s1}{s2[::-1]}')

file = 'input.txt'
# file = 'example_01.txt.txt'
# file = 'example_02.txt.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

grid = np.full((len(data), len(data[0])), '.')
decode(1000, 1000_000_000_000, data)

print(f'\nFinal decoded message:\n')
for line in grid:
    print(''.join(line))
