file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

total_stones, blinks = 0, 25
stones = data[0].split()
for _ in range(blinks):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            s1, s2 = stone[:len(stone) // 2], stone[len(stone) // 2:]
            while s2[0] == '0':
                if len(s2) == 1:
                    break
                s2 = s2[1:]
            new_stones.append(s1)
            new_stones.append(s2)
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones[:]
print(f'Part 1: {len(stones)}')

stones = {n: 1 for n in data[0].split()}
blinks = 75
for _ in range(blinks):
    new_stones = dict()
    for stone in stones:
        if stone == '0':
            if '1' not in new_stones:
                new_stones['1'] = stones[stone]
            else:
                new_stones['1'] += stones[stone]
        elif len(stone) % 2 == 0:
            s1, s2 = stone[:len(stone) // 2], stone[len(stone) // 2:]
            while s2[0] == '0':
                if len(s2) == 1:
                    break
                s2 = s2[1:]
            for s in s1, s2:
                if s not in new_stones:
                    new_stones[s] = stones[stone]
                else:
                    new_stones[s] += stones[stone]
        else:
            s = str(int(stone) * 2024)
            if s not in new_stones:
                new_stones[s] = stones[stone]
            else:
                new_stones[s] += stones[stone]
    stones = new_stones.copy()
print(f'Part 2: {sum(map(int, stones.values()))}')
