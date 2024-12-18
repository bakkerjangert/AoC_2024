import numpy as np
from collections import defaultdict

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

file = 'input.txt'
# file = 'example_01.txt'

# Import Grid structure
grid = np.array([list(line.strip()) for line in open(file)])

directions = {'<': (-1, 0), '^': (0, -1), '>': (1, 0), 'v': (0, 1)}
walk, turn = 1, 1000
links = defaultdict(list)
blinks = defaultdict(list)
S, E = (np.where(grid == 'S')[1][0], np.where(grid == 'S')[0][0]), (np.where(grid == 'E')[1][0], np.where(grid == 'E')[0][0])

nodes = np.where(grid == '.')
nodes = list(zip(nodes[1], nodes[0]))
nodes.insert(0, S), nodes.append(E)
total_nodes = list()
for node in nodes:
    for i, d in enumerate('<^>v'):
        x, y, cur_node = node[0], node[1], node + (d, )
        total_nodes.append(cur_node)
        nx, ny = x + directions[d][0], y + directions[d][1]
        px, py = x - directions[d][0], y - directions[d][1]
        if grid[ny, nx] in '.ES':
            links[cur_node].append((nx, ny, d, walk))
        if grid[py, px] in '.ES':
            blinks[cur_node].append((px, py, d))
        for d2 in ('<^>v'[i - 1], '<^>v'[(i + 1) % 4]):
            links[cur_node].append((x, y, d2, turn))
            blinks[cur_node].append((x, y, d2))

S = S + ('>',)  # Facing east
ends = [E + (d,) for d in '<^>v']
scores = {n: [float('inf'), tuple()] for n in total_nodes}
pos_S = tuple(S[:])
scores[S] = [0, (pos_S,)]

unvisited_nodes, visited_nodes = total_nodes[:], []
finished = False
min_path_score = None
while len(unvisited_nodes) != 0:
    next_node, s = None, [float('inf'), tuple()]
    for node in unvisited_nodes:
        if scores[node][0] < s[0]:
            next_node, s = node, scores[node]
    if next_node in ends and not finished:
        print(f'Part 1: {s[0]}')
        min_path_score = s[0]
        finished = True
    unvisited_nodes.remove(next_node)
    for n in links[next_node]:
        if scores[n[:-1]][0] < s[0] + n[3]:
            continue
        new_score = min(scores[n[:-1]][0], s[0] + n[3])
        path = s[1] + (n[:3],)
        scores[n[:-1]] = [new_score, path]

# Part 2
end_paths = []
for score in scores.values():
    if score[0] == min_path_score and score[1][-1] in ends:
        end_paths.append((score[0], (score[1][-1],)))
        len_path = len(score[1])

finished = False
while not finished:
    # print('HERE1')
    new_end_paths = []
    while end_paths:
        n1 = end_paths.pop()
        # grid[n1[1][1], n1[1][0]] = 'O'
        for n2 in blinks[n1[1][0]]:
            if n2 == S:
                finished = True
            ds = 1 if n1[1][0][2] == n2[2] else 1000  #
            if n1[0] - ds == scores[n2][0] and n2 not in n1[1]:
                new_end_paths.append((n1[0] - ds, ((n2,) + (n1[1]))))
    end_paths = new_end_paths[:]

for p in end_paths:
    if len(p[1]) == len_path and p[1][0] == S:
        for x, y, d in p[1]:
            grid[y, x] = 'O'

print(f'Part 2: {np.count_nonzero(grid == "O")}')
# show_grid(grid)

# Part 2: 512 is too high
# Part 2: 450 is too high