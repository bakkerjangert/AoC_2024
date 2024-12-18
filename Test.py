
scores = {'a': 0, 'b': 0, 'c': 0}

n = min(scores, key=scores.get)

print(n)