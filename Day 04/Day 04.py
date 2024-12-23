file = 'input.txt'
# file = 'example_01.txt.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

def check_word(check_x, check_y):
    for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
        word = True
        x, y = check_x, check_y
        for char in 'XMAS':
            if data[y][x] != char:
                word = False
                break
            if char != 'S':
                x, y = x + dx, y + dy
            if not 0 <= x < len(data[0]) or not 0 <= y < len(data):
                word = False
                break
        if word:
            word_count[0] += 1

def check_x(x, y):
    string1 = data[y][x] + data[y + 1][x + 1] + data[y + 2][x + 2]
    if string1 == 'MAS' or string1 == 'SAM':
        string2 = data[y + 2][x] + data[y + 1][x + 1] + data[y][x + 2]
        if string2 == 'MAS' or string2 == 'SAM':
            word_count[1] += 1


word_count = [0, 0]
for x in range(len(data[0])):
    for y in range(len(data)):
        check_word(x, y)
        if x < len(data[0]) - 2 and y < len(data) - 2:
            check_x(x, y)
print(f'Part 1: {word_count[0]}')
print(f'Part 2: {word_count[1]}')