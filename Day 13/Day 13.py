file = 'input.txt'
# file = 'example_01.txt.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()
if data[-1] != '':
    data.append('')

a, b, p = None, None, None
answer_pt1 = 0
for line in data:
    a = (int(line.split('X')[1].split(',')[0]), int(line.split('Y')[1])) if 'A' in line else a
    b = (int(line.split('X')[1].split(',')[0]), int(line.split('Y')[1])) if 'B' in line else b
    p = (int(line.split('X=')[1].split(',')[0]), int(line.split('Y=')[1])) if 'Prize' in line else p
    if line == '':
        minimum_tokes = float('inf')
        for pa in range(1, 101):
            for pb in range(1, 101):
                x, y = pa * a[0] + pb* b[0], pa * a[1] + pb * b[1]
                if x == p[0] and y == p[1]:
                    minimum_tokes = min(pa * 3 + pb, minimum_tokes)
        if isinstance(minimum_tokes, int):
            answer_pt1 += minimum_tokes
print(f'Part 1: {answer_pt1}')

val = 10_000_000_000_000
answer_pt2 = 0
for line in data:
    a = (int(line.split('X')[1].split(',')[0]), int(line.split('Y')[1])) if 'A' in line else a
    b = (int(line.split('X')[1].split(',')[0]), int(line.split('Y')[1])) if 'B' in line else b
    p = (int(line.split('X=')[1].split(',')[0]) + val, int(line.split('Y=')[1]) + val) if 'Prize' in line else p
    if line == '':
        xa, ya, xb, yb, xp, yp = (a[0], a[1], b[0], b[1], p[0], p[1])
        b = (yp - xp * ya / xa) / (yb - (xb * ya / xa))
        a = (xp - b * xb) / xa
        a, b = round(a), round(b)
        if a * xa + b * xb == xp and a * ya + b * yb == yp and a >= 0 and b >= 0:
            answer_pt2 += a * 3 + b
print(f'Part 2: {answer_pt2}')



