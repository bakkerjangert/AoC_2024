file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

x_max, y_max = len(data), len(data[0])
positions = []
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '0':
            val = [(x, y), (x, y)]
            positions.append(val)  # starting position and next position

for val in list('123456789'):
    next_positions = []
    for pos in positions:
        for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = pos[1][0] + direction[0], pos[1][1] + direction[1]
            if not 0 <= new_x < x_max or not 0 <= new_y < y_max:
                continue
            if data[new_y][new_x] == val:
                new_pos = pos[:]
                new_pos[1] = (new_x, new_y)
                next_positions.append(new_pos)
    positions = next_positions[:]
answer_pt2 = len(positions)
positions = set(map(tuple, positions))
print(f'Part 1: {len(positions)}')
print(f'Part 2: {answer_pt2}')
