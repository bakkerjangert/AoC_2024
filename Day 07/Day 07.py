from itertools import product
file = 'input.txt'
# file = 'example_01.txt.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

def list_pt1(n):
    return tuple(product([mul, add], repeat=n))

def list_pt2(n):
    return tuple(product([mul, add, concat], repeat=n))

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def concat(a, b):
    return int(str(a) + str(b))

def check_line(string, pt1=True):
    answer = int(string.split(': ')[0])
    n = list(map(int, string.split(': ')[1].split(' ')))
    list_of_operators = list_pt1(len(n) - 1) if pt1 else list_pt2(len(n) - 1)
    for operators in list_of_operators:
        result = n[0]
        for b, operator in zip(n[1:], operators):
            result = operator(result, b)
            if result > answer:
                break
        if result == answer:
            return answer
    return 0

# def check_line(string, pt1=True):
#     answer = int(string.split(': ')[0])
#     n = list(map(int, string.split(': ')[1].split(' ')))
#     list_of_operators = list_pt1(len(n) - 1) if pt1 else list_pt2(len(n) - 1)
#     for operators in list_of_operators:
#         numbers = n[:]
#         for operator in operators:
#             n1, n2 = numbers[0], numbers[1]
#             del numbers[0]
#             numbers[0] = operator(n1, n2)
#         if numbers[0] == answer:
#             return answer
#     return 0

answer_pt1 = 0
for line in data:
    answer_pt1 += check_line(line)
print(f'Part 1 = {answer_pt1}')

answer_pt2 = 0
for line in data:
    answer_pt2 += check_line(line, pt1=False)
print(f'Part 2 = {answer_pt2}')