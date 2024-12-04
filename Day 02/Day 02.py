def check_report(r):
    increasing, decreasing = False, False
    max_delta, min_delta = 0, 9999999999999999
    for n1, n2 in zip(r, r[1:]):
        if n1 < n2:
            increasing = True
        elif n1 > n2:
            decreasing = True
        max_delta = max(abs(n1 - n2), max_delta)
        min_delta = min(abs(n1 - n2), min_delta)
    if not (increasing and decreasing) and min_delta >= 1 and max_delta <= 3:
        return True
    else:
        return False

def check_report_part2(r, first=True):
    order, delta, faulty_index = [], [], set()
    for i, (n1, n2) in enumerate(zip(r, r[1:])):
        order.append(1 if n2 - n1 > 0 else -1)
        delta.append(abs(n1 - n2))
        if not 0 < delta[-1] < 4:
            faulty_index.add(i)
    val = 1 if order.count(1) >= order.count(-1) else -1
    for i, v in enumerate(order):
        if v != val:
            faulty_index.add(i)
    if len(faulty_index) == 0:
        answer[0] += 1
        answer[1] += 1
    elif len(faulty_index) == 1:
        i = faulty_index.pop()
        if i == 0 or i == len(order) - 1:  # Fault at edge --> deleting edge results in safe report
            answer[1] += 1
        else:
            # try left-side; ommit position i
            val_left = 1 if r[i + 1] - r[i - 1] > 0 else -1
            check_left = val_left == val and 0 < abs(r[i - 1] - r[i + 1]) < 4
            # try right-side; ommit position i
            val_right = 1 if r[i + 2] - r[i] > 0 else -1
            check_right = val_right == val and 0 < abs(r[i] - r[i + 2]) < 4
            if check_left or check_right:
                answer[1] += 1
    elif len(faulty_index) == 2:
        i1, i2 = tuple(faulty_index)
        print(f'Len = 2 at {i1, i2}, {r}, val = {val}')
        if abs(i1 - i2) != 1:
            print(f'Incorrect; di > 1\n')
            # faulty values not adjacent; Faulty report
            pass
        elif len(order) == 4 and (i1 == 0 or i2 == 3):
            # Edge case --> 4 values, 2 increase and 2 decrease at sides!
            for r1 in (r[0:1] + r[2:], r[0:3] + r[4:]):
                if r1 == sorted(r1) or r1 == sorted(r1, reverse=True):
                    check = True
                    for n1, n2 in zip(r1, r1[1:]):
                        if not 0 < abs(n1 - n2) < 4:
                            check = False
                    if check:
                        print('Edge Case --> correct!\n')
                        answer[1] += 1
            # val_left = 1 if r[2] - r[0] > 0 else -1
            # check_left = val_left == order[-1] and 0 < abs(r[0] - r[2]) < 4
            # val_right = 1 if r[4] - r[2] > 0 else -1
            # check_right = val_right == order[0] and 0 < abs(r[2] - r[4]) < 4
            # if check_left or check_right:
            #
            #     answer[1] += 1
        else:
            val_mid = 1 if r[i2 + 1] - r[i1] > 0 else -1
            check_mid = val_mid == val and 0 < abs(r[i1] - r[i2 + 1]) < 4
            if check_mid:
                print('Mid case --> correct!\n')
                answer[1] += 1

file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

answer = [0, 0]
for r in data:
    report = list(map(int, r.split()))
    check_report_part2(report)
print(f'Part 1: {answer[0]}')
print(f'Part 2: {answer[1]}')

# 588 to low

# 590 incorrect (guess 3)

# 592 to high