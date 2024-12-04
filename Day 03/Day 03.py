file = 'input.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

answer_pt1, answer_pt2 = 0, 0
m = True
for line in data:
    muls = line.split('mul(')
    for mul in muls:
        if ')' in mul:
            n = mul.split(')')[0]
            try:
                numbers = list(map(int, n.split(',')))
                if len(numbers) == 2 and 0 < numbers[0] < 1000 and 0 < numbers[1] < 1000:
                    answer_pt1 += numbers[0] * numbers[1]
                    if m:
                        answer_pt2 += numbers[0] * numbers[1]
            except:
                pass
        if 'do()' in mul and "don't()" in mul:
            i_do, i_dont = mul.rfind('do()'), mul.rfind("don't()")
            m = True if i_do > i_dont else False
        elif 'do()' in mul:
            m = True
        elif "don't()" in mul:
            m = False
print(f'Part 1: {answer_pt1}')
print(f'Part 2: {answer_pt2}')
