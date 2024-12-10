file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

disk = tuple(map(int, list(data[0])))
written_length = 0
for i, n in enumerate(disk):
    if i % 2 == 0:
        written_length += n
written_disk = []

write = True
i_last = len(disk) - 1 if len(disk) % 2 == 1 else len(disk) - 2
n_last = disk[i_last]
for i, n in enumerate(disk):
    if i % 2 == 0:
        for _ in range(n):
            written_disk.append(i // 2)
            if len(written_disk) == written_length:
                write = False
                break
    else:
        for _ in range(n):
            written_disk.append(i_last // 2)
            if len(written_disk) == written_length:
                write = False
                break
            n_last -= 1
            if n_last == 0:
                i_last -= 2
                n_last = disk[i_last]
    if not write:
        break

answer_pt1 = 0
for i, n in enumerate(written_disk):
    answer_pt1 += i * n
print(f'Part 1: {answer_pt1}')

free_spaces, shifted_is = dict(), []
written_disk = ''
i_last = len(disk) - 1 if len(disk) % 2 == 1 else len(disk) - 2
for i, n in enumerate(disk):
    if i % 2 == 1:
        free_spaces[i] = [n]
for i in range(i_last, 0, -2):
    n = disk[i]
    for j in sorted(free_spaces.keys()):
        if j > i:
            break
        if free_spaces[j][0] >= n:
            shifted_is.append(i)
            free_spaces[j][0] -= n
            free_spaces[j].append((i, n))
            break
answer_pt2, counter = 0, 0
for i, n in enumerate(disk):
    if i in free_spaces.keys():
        for moved_block in free_spaces[i][1:]:
            for _ in range(moved_block[1]):
                answer_pt2 += moved_block[0] // 2 * counter
                counter += 1
                written_disk += str(moved_block[0] // 2)
        counter += free_spaces[i][0]
        written_disk += '.' * free_spaces[i][0]
    elif i in shifted_is:
        counter += disk[i]
        written_disk += '.' * disk[i]
    else:
        for _ in range(n):
            answer_pt2 += i // 2 * counter
            counter += 1
            written_disk += str(i // 2)
# print(written_disk)
print(f'Part 2: {answer_pt2}')

# Too high = 8664287909542