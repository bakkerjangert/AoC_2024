import numpy as np
from collections import defaultdict

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

file = 'input.txt'
file = 'example_02.txt'

# Import Grid structure
grid = np.array([list(line.strip()) for line in open(file)])

directions = {'<': (-1, 0), '^': (0, -1), '>': (1, 0), 'v': (0, 1)}
walk, turn = 1, 1000
links = defaultdict(list)
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
        if grid[ny, nx] in '.E':
            links[cur_node].append((nx, ny, d, walk))
        for d2 in ('<^>v'[i - 1], '<^>v'[(i + 1) % 4]):
            links[cur_node].append((x, y, d2, turn))

S = S + ('>',)  # Facing east
ends = [E + (d,) for d in '<^>v']
scores = {n: [float('inf'), tuple(tuple())] for n in total_nodes}
pos_S = tuple(S[:-1])
scores[S] = [0, (pos_S,)]
print(scores[S])

# for item in links.items():
#     print(item)

unvisited_nodes, visited_nodes = total_nodes[:], []
finished = False
min_path_score = None
while len(unvisited_nodes) != 0:
    next_node, s = None, [float('inf'), tuple()]
    for node in unvisited_nodes:
        if scores[node][0] < s[0]:
            next_node, s = node, scores[node]
    # print(f'Next node {next_node} with score {s}')
    if next_node in ends and not finished:
        print(f'Part 1: {s[0]}')
        min_path_score = s[0]
        finished = True
    unvisited_nodes.remove(next_node)
    for n in links[next_node]:
        if scores[n[:-1]][0] <= s[0] + n[3]:
            continue
        new_score = min(scores[n[:-1]][0], s[0] + n[3])
        new_x, new_y = n[:2]
        new_paths =
        scores[n[:-1]] = [new_score, new_paths]

for score in scores.values():
    if score[0] == min_path_score:
        for p in score[1]:
            for c in p:
                grid[c[1], c[0]] = 'O'
show_grid(grid)


