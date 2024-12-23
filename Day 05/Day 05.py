file = 'input.txt'
# file = 'example_01.txt.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

before, after = dict(), dict()
reports, incorrect_reports = [], []

for line in data:
    if '|' in line:
        n1, n2 = map(int, line.split('|'))
        if n1 not in before:
            before[n1] = [n2]
        else:
            before[n1].append(n2)
        if n2 not in after:
            after[n2] = [n1]
        else:
            after[n2].append(n1)
    if ',' in line:
        reports.append(list(map(int, line.split(','))))

answer_pt1 = 0
for report in reports:
    safe = True
    for i, n in enumerate(report[:-1]):
        # Check before
        if n in before:
            for n2 in before[n]:
                if n2 in report:
                    if n2 not in report[i:]:
                        safe = False
                        break
        if not safe:
            break
        # check after:
        if n in after:
            for n2 in after[n]:
                if n2 in report:
                    if n2 not in report[:i]:
                        safe = False
                        break
        if not safe:
            break
    if safe:
        answer_pt1 += report[len(report) // 2]
    else:
        incorrect_reports.append(report)
print(f'Part 1: {answer_pt1}')

answer_pt2 = 0
for i, report in enumerate(incorrect_reports):
    correct_report = []
    while len(report) != 0:
        for n in report[:]:
            if n in after:
                remove_n = True
                for n2 in after[n]:
                    if n2 in report:
                        remove_n = False
                        break
                if remove_n:
                    correct_report.append(n)
                    report.remove(n)
            else:
                correct_report.append(n)
                report.remove(n)
    answer_pt2 += correct_report[len(correct_report) // 2]
print(f'Part 2: {answer_pt2}')