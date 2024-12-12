from collections import Counter, defaultdict
from itertools import combinations, product, permutations

import numpy as np

def show_grid(grd):
    print(f'\n---- GRID ----\n')
    for line in grd:
        for char in line:
            print(char, end='')
        print('')


file = 'example_01.txt'

# Import Grid structure
grid = np.array([list(line.strip()) for line in open(file)])

# Import string
string = open(file, 'r').read()
counted = Counter(open(file, 'r').read())
print(counted)

# Import numbers
int_lists = [[int(num) for num in line.split()] for line in open('numbers.txt')]
print(int_lists)

defdic = defaultdict(int)
for n in [item for sublist in int_lists for item in sublist]:
    defdic[n] += 1
print(defdic)

# Itertools
print('Permutations abc')
for p in permutations(tuple('abc')):
    print(p)

print('Combinations abcdef')
for c in combinations(tuple('abcdef'), 2):
    print(c)