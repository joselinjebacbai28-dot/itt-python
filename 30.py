from itertools import permutations
s, k = input().split()
s_sorted = sorted(s)
k = int(k)
result = list(permutations(s_sorted, k))
for p in result:
    print("".join(p))
