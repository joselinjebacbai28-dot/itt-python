
from itertools import groupby


s = input()

result = []
for k, g in groupby(s):
    result.append((len(list(g)), int(k)))


print(*result)
