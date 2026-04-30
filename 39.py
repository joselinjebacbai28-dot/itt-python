m_size = int(input())
m_set = set(map(int, input().split()))

n_size = int(input())
n_set = set(map(int, input().split()))

sym_diff = m_set.symmetric_difference(n_set)

for value in sorted(sym_diff):
    print(value)
