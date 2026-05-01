n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
data.sort(key=lambda x: x[k])
for row in data:
    print(' '.join(map(str, row)))
