
from itertools import combinations

s, k = input().split()

s_sorted = "".join(sorted(s))
k = int(k)

for i in range(1, k + 1):
    res = list(combinations(s_sorted, i))
   
    for c in res:
        print("".join(c))
