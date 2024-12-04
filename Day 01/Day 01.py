file = 'input.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

l1, l2 = list(), list()

for row in data:
    l1.append(int(row.split('   ')[0])), l2.append(int(row.split('   ')[1]))

l1.sort(), l2.sort()

delta = 0
for n1, n2 in zip(l1, l2):
    delta += abs(n1 - n2)
print(f'Part 1: {delta}')

similarity_score = 0
for n in l1:
    similarity_score += n * l2.count(n)
print(f'Part 2: {similarity_score}')