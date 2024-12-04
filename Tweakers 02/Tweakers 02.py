from collections import deque


def decode(n, data):
    l = len(data[0])
    s1, s2 = '', ''
    for i in range(l // 2):
        print(f'\ni = {i}')
        string = data[i][i: l - i]
        print(string)
        for j in range(i + 1, l - i - 1):
            string += data[j][l - i - 1]
        print(string)
        string += data[l - i - 1][i: l - i][::-1]
        print(string)
        for k in range(l - i - 2, i, -1):
            print(f'k = {k}')
            string += data[k][i]
        print(string)
        dq = deque(list(string))
        dq.rotate(n)
        print(dq[0], dq[len(dq) // 2])
        s1 += dq[0]
        s2 += dq[len(dq) // 2]
    print(s1 + s2[::-1])
file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

decode(1000, data)
