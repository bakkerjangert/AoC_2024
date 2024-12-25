import random

def AND(a, b):
    return 1 if a == b == 1 else 0

def OR(a, b):
    return 1 if a == 1 or b == 1 else 0

def XOR(a, b):
    return 1 if a != b else 0

def check_dict(dct):
    solved = {k: dct[k] for k in dct.keys() if dct[k] in (0, 1)}
    unsolved = {k: dct[k] for k in dct.keys() if not dct[k] in (0, 1)}
    changed = True
    while len(unsolved) > 0 and changed:
        changed = False
        for k in list(unsolved.keys()):
            v1, f, v2 = unsolved[k]
            if v1 in solved and v2 in solved:
                solved[k] = func[f](solved[v1], solved[v2])
                del unsolved[k]
                changed = True
    if changed:
        x, y, z = '', '', ''
        for ky in sorted([k for k in solved if k[0] == 'x']):
            x += '1' if solved[ky] else '0'
        for ky in sorted([k for k in solved if k[0] == 'y']):
            y += '1' if solved[ky] else '0'
        for ky in sorted([k for k in solved if k[0] == 'z']):
            z += '1' if solved[ky] else '0'
        x, y, z = int(x[::-1], 2), int(y[::-1], 2), int(z[::-1], 2)
        if x + y == z:
            return True
    return False

file_pt1 = 'input.txt'
file_pt2 = 'input_switch.txt'
# file = 'example_01.txt'
# file = 'example_02.txt'

with open(file_pt1, encoding="utf8") as f:
    data = f.read().splitlines()

func = {'AND': AND, 'OR': OR, 'XOR': XOR}

solved = dict()
unsolved = dict()

for line in data:
    if ':' in line:
        val = 1 if line[-1] ==  '1' else 0
        solved[line.split(':')[0]] = val
    elif '->' in line:
        unsolved[line.split('-> ')[-1]] = tuple(line.split(' ')[0:3])

while len(unsolved) > 0:
    for k in list(unsolved.keys()):
        v1, f, v2 = unsolved[k]
        if v1 in solved and v2 in solved:
            solved[k] = func[f](solved[v1], solved[v2])
            del unsolved[k]

string = ''
for ky in sorted([k for k in solved if k[0] == 'z']):
    string += str(solved[ky])
zstring = string[::-1]
z = int(string[::-1],2)
print(f'Part 1: {int(string[::-1],2)}')

# Part 2: Manually solved. Input did not reveal last error, so used a random x instead (algorithm valid for all numbers)
with open(file_pt2, encoding="utf8") as f:
    data = f.read().splitlines()

solved = dict()
unsolved = dict()

for line in data:
    if ':' in line:
        val = 1 if line[-1] ==  '1' else 0
        solved[line.split(':')[0]] = val
    elif '->' in line:
        unsolved[line.split('-> ')[-1]] = tuple(line.split(' ')[0:3])

x = random.randint(10_000_000_000_000, 50_999_999_999_999)
keys = ["x{:02d}".format(i) for i in range(0, 44 + 1)]

for i, c in enumerate(bin(x)[2:][::-1]):
    solved[keys[i]] = int(c)

while len(unsolved) > 0:
    for k in list(unsolved.keys()):
        v1, f, v2 = unsolved[k]
        if v1 in solved and v2 in solved:
            solved[k] = func[f](solved[v1], solved[v2])
            del unsolved[k]

string = ''
for ky in sorted([k for k in solved if k[0] == 'x']):
    string += str(solved[ky])
xstring = '0' + string[::-1]
x = int(string[::-1],2)

string = ''
for ky in sorted([k for k in solved if k[0] == 'y']):
    string += str(solved[ky])
ystring = '0' + string[::-1]
y = int(string[::-1],2)

string = ''
for ky in sorted([k for k in solved if k[0] == 'z']):
    string += str(solved[ky])
zstring = string[::-1]
z = int(string[::-1],2)

print(xstring)
print(ystring)
print('-' * len(xstring))
print(bin(x + y)[2:])
print(zstring)

print(f'{x} + {y} = {z} --> {x + y == z}')

print(','.join(sorted(('nbc', 'svm', 'kqk', 'z15', 'z39', 'fnr', 'z23', 'cgq'))))


