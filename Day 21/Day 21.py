from collections import defaultdict, Counter
import numpy as np


def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')

def get_path_n(n):
    paths = set(('',))
    for step in zip(n[:-1], n[1:]):
        new_paths = set()
        for path in paths:
            for p in n_paths[step]:
                new_paths.add(path + p + 'A')
        paths = new_paths.copy()
    return paths

def get_path_n2(n):
    path = ''
    for step in zip(n[:-1], n[1:]):
        p = n_paths[step][0]
        path += p + 'A'
    return path

def get_path_d(n, return_min=True):
    paths = set(('',))
    for step in zip(n[:-1], n[1:]):
        new_paths = set()
        for path in paths:
            for p in d_paths[step]:
                new_paths.add(path + p + 'A')
        paths = new_paths.copy()
    return paths

def get_path_d2(n):
    path = ''
    for step in zip(n[:-1], n[1:]):
        p = d_paths[step][0]
        path += p + 'A'
    return path


file = 'input.txt'
# file = 'example_01.txt.txt'


with open(file, encoding="utf8") as f:
    codes = f.read().splitlines()

r = {'<': '>', '>': '<', '^': 'v', 'v': '^'}

numeric = np.array([['7', '8', '9'],
                    ['4', '5', '6'],
                    ['1', '2', '3'],
                    ['.', '0', 'A']],)

directional = np.array([['.', '^', 'A'],
                        ['<', 'v', '>']],)


n_paths, d_paths = defaultdict(tuple), defaultdict(tuple)
ns = '7894561230A'
ds = '^A<v>'


for i in range(len(ns) - 1):
    for j in range(i, len(ns)):
        if i == j:
            n_paths[(ns[i], ns[j])] += ('',)
            continue
        x1, y1 = int(np.where(numeric == ns[i])[1][0]), int(np.where(numeric == ns[i])[0][0])
        x2, y2 = int(np.where(numeric == ns[j])[1][0]), int(np.where(numeric == ns[j])[0][0])
        p = ''
        # hor - vert
        p += '>' * (x2 - x1) if x2 > x1 else '<' * (x1 - x2) if x1 > x2 else ''
        p += 'v' * (y2 - y1) if y2 > y1 else '^' * (y1 - y2) if y1 > y2 else ''
        n_paths[(ns[i], ns[j])] += (p,)
        n_paths[(ns[j], ns[i])] += (''.join([r[c] for c in p[::-1]]),)
        # vert - hor
        if not (x1 == 0 and y2 == 3) and not (x1 - x2 == 0 or y1 - y2 == 0):
            p = ''
            p += 'v' * (y2 - y1) if y2 > y1 else '^' * (y1 - y2) if y1 > y2 else ''
            p += '>' * (x2 - x1) if x2 > x1 else '<' * (x1 - x2) if x1 > x2 else ''
            n_paths[(ns[i], ns[j])] += (p,)
            n_paths[(ns[j], ns[i])] += (''.join([r[c] for c in p[::-1]]),)
n_paths[(ns[-1], ns[-1])] += ('',)

for i in range(len(ds) - 1):
    for j in range(i, len(ds)):
        if i == j:
            d_paths[(ds[i], ds[j])] += ('',)
            continue
        x1, y1 = int(np.where(directional == ds[i])[1][0]), int(np.where(directional == ds[i])[0][0])
        x2, y2 = int(np.where(directional == ds[j])[1][0]), int(np.where(directional == ds[j])[0][0])
        p = ''
        # vert - hor
        p += 'v' * (y2 - y1) if y2 > y1 else '^' * (y1 - y2) if y1 > y2 else ''
        p += '>' * (x2 - x1) if x2 > x1 else '<' * (x1 - x2) if x1 > x2 else ''
        d_paths[(ds[i], ds[j])] += (p,)
        d_paths[(ds[j], ds[i])] += (''.join([r[c] for c in p[::-1]]),)
        # hor - vert
        if not x2 == 0 and not (x1 - x2 == 0 or y1 - y2 == 0):
            p = ''
            p += '>' * (x2 - x1) if x2 > x1 else '<' * (x1 - x2) if x1 > x2 else ''
            p += 'v' * (y2 - y1) if y2 > y1 else '^' * (y1 - y2) if y1 > y2 else ''
            d_paths[(ds[i], ds[j])] += (p,)
            d_paths[(ds[j], ds[i])] += (''.join([r[c] for c in p[::-1]]),)
d_paths[(ds[-1], ds[-1])] += ('',)

for item in n_paths.items():
    print(item)

answer_pt1 = 0
for code in codes:
    r1_paths = get_path_n('A' + code)
    r2_paths = set()
    for p in r1_paths:
        r2_paths.update(get_path_d('A' + p))
    s_paths = set()
    for p2 in r2_paths:
        s_paths.update(get_path_d('A' + p2))
    min_length = min(len(item) for item in s_paths)
    val = int(code.replace('A', ''))
    # print(f'{code} added {val} x {min_length}')
    answer_pt1 += val * min_length
    # print(Counter([len(s[0]) for s in s_paths]))
print(f'Part 1: {answer_pt1}')

counts = dict()
for k in d_paths.keys():
    if len(d_paths[k][0]) < 2:
        counts[k] = len(d_paths[k][0])
    elif len(d_paths[k][0]) == 2:
        val = d_paths[k][0]
        print(k, d_paths[k], d_paths[(val[0], val[1])])
        lengths = [len(d_paths[(i[0], i[1])][0]) for i in d_paths[k]]
        counts[k] = 2 + min(lengths)
    else:
        counts[k] = 5


answer_pt2 = 0
for code in codes:
    paths = get_path_n('A' + code)
    for r in range(25):
        count = float('inf')
        print(r)
        new_paths = set()
        for p in paths:
            counter = Counter(zip(p[:-1], p[1:]))
            val = sum([counter[c] * counts[c] for c in counter])
            if val < count:
                count = val
                new_paths = set()
            elif val > count:
                continue
            new_paths.update(get_path_d(p))
        min_length = min([len(p) for p in new_paths])
        paths = set([p for p in new_paths if len(p) == min_length])
    val = int(code.replace('A', ''))
    answer_pt2 += val * len(paths.pop())
print(f'Part 2: {answer_pt2}')