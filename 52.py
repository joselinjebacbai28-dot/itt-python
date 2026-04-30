
from itertools import product

# Read K (number of lists) and M (modulo value)
k, m = map(int, input().split())

lists = []
for _ in range(k):
    # input().split()[1:] skips the count 'Ni' and takes the actual numbers
    row = map(int, input().split()[1:])
    lists.append([x**2 for x in row])

max_val = 0
for combination in product(*lists):
    # Sum the squares and take the modulo M
    current_sum = sum(combination) % m
    # Update max_val if we find a higher result
    if current_sum > max_val:
        max_val = current_sum

print(max_val)
