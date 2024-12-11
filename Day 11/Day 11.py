from collections import Counter, defaultdict

def calculate_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = defaultdict(int)
        for stone in stones:
            if stone == '0':
                new_stones['1'] += stones[stone]
            elif len(stone) % 2 == 0:
                s1, s2 = stone[:len(stone) // 2], stone[len(stone) // 2:]
                s2 = s2.lstrip('0') if s2.count('0') != len(s2) else '0'
                for s in s1, s2:
                    new_stones[s] += stones[stone]
            else:
                new_stones[str(int(stone) * 2024)] += stones[stone]
        stones = new_stones.copy()
    return sum(stones.values())

file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

print(f'Part 1: {calculate_stones(Counter(data[0].split()), 25)}')
print(f'Part 2: {calculate_stones(Counter(data[0].split()), 75)}')
