
from itertools import combinations_with_replacement

s, k = input().split()

s_sorted = sorted(s)
k = int(k)

result = combinations_with_replacement(s_sorted, k)

for item in result:
    print("".join(item))
