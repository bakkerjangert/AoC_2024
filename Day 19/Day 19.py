def can_build_string(target_string, substrings):
    dp = [0] * (len(target_string) + 1)
    dp[0] = 1  # Empty string can be built
    # Check for each position i if the string[:i] can be built up by adding one of the substrings
    # keep counters for possible number of buildups
    for i in range(1, len(target_string) + 1):
        for substring in substrings:
            if i >= len(substring):
                if dp[i - len(substring)] > 0:
                    if target_string[i - len(substring):i] == substring:
                        dp[i] += dp[i - len(substring)]
    return dp[-1]

def can_build_string_own(target_string, substrings):
    dp = [0] * (len(target_string) + 1)
    dp[0] = 1  # Empty string can be built
    # Check for each position i if the string[:i] can be built up by adding one of the substrings
    # keep counters for possible number of buildups

    for i in range(1, len(target_string) + 1):
        for substring in substrings:
            if i >= len(substring):
                if dp[i - len(substring)] > 0:
                    if target_string[i - len(substring):i] == substring:
                        dp[i] += dp[i - len(substring)]
    return dp[-1]

file = 'input.txt'
# file = 'example_01.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

towels, patterns = None, []
for line in data:
    if ',' in line:
        towels = line.split(', ')
    elif line != '':
        patterns.append(line)

answer_pt1, answer_pt2 = 0, 0
for pattern in patterns:
    val = can_build_string(pattern, towels)
    if val > 0:
        answer_pt1 += 1
        answer_pt2 += val
print(f'Part 1: {answer_pt1}')
print(f'Part 2: {answer_pt2}')
