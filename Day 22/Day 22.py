from collections import Counter, defaultdict
from functools import cache

@cache
def update(n):
    n = (n ^ (n * 64)) % prune_val
    n = (n ^ (n // 32)) % prune_val
    n = (n ^ (n * 2048)) % prune_val
    return n

file = 'input.txt'
# file = 'example_01.txt.txt'

with open(file, encoding="utf8") as f:
    secret_numbers = f.read().splitlines()

prune_val = 16777216

answer_pt1 = 0
monkey_prizes = []
monkey_bananas = defaultdict(int)
for n in secret_numbers:
    m = n[-1]
    n = int(n)
    for s in range(2000 - 1):
        prev_price = str(n)[-1]
        n = update(n)
        m += str(n)[-1]
    answer_pt1 += n
    monkey_prizes.append(m)
print(f'Part 1: {answer_pt1}')

monkey_deltas = []
for i, m in enumerate(monkey_prizes):
    # print(f'Monkey {i + 1} Deltas')
    sequence = []
    for a, b in zip(m[:-1], m[1:]):
        a, b = map(int, (a, b))
        sequence.append(b - a)
    monkey_deltas.append(tuple(sequence))

all_monkey_sequences = Counter()
for i, m in enumerate(monkey_deltas):
    # print(f'Monkey {i + 1} Sequences')
    sequences = set()
    j = 0
    for a, b, c, d in zip(m[:], m[1:], m[2:], m[3:]):
        if (a, b, c, d) not in sequences:
            monkey_bananas[(a, b, c, d)] += int(monkey_prizes[i][j + 4])
        sequences.add((a, b, c, d))
        j += 1
    all_monkey_sequences.update(sequences)
print(f'Part 2: {max(monkey_bananas.values())}')
