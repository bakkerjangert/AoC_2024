from collections import defaultdict

def check_network(connections):
    invalids = set()
    for i, c1 in enumerate(connections[:-1]):
        for j, c2 in enumerate(connections[i + 1:]):
            if c2 not in con[c1]:
                invalids.add(c1)
                invalids.add(c2)
    if len(invalids) == 0:
        return list()
    else:
        new_connections = []
        for invalid in invalids:
            new_connection = sorted(connections[:])
            new_connection.remove(invalid)
            new_connections.append(new_connection)
        return new_connections

file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

con = defaultdict(list)

for connection in data:
    c1, c2 = connection.split('-')
    if c1 == c2:
        continue
    con[c1].append(c2)
    con[c2].append(c1)

set_of_three = set()
for k, v in con.items():
    if len(v) > 1:
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                if v[i] in con[v[j]]:
                    set_of_three.add(tuple(sorted((v[i], v[j], k))))

answer_part_1 = 0
for c1, c2, c3 in set_of_three:
    if c1[0] == 't' or c2[0] == 't' or c3[0] == 't':
        answer_part_1 += 1
print(f'Part 1: {answer_part_1}')

connections = []
for k, v in con.items():
    connections.append([k,] + v[:])

while len(connections) > 0:
    cs = connections.pop(0)
    new_cs = check_network(cs)
    if len(new_cs) == 0:
        print(f'Part 2: {','.join(sorted(cs))}')
        break
    else:
        connections += new_cs
