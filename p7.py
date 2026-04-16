
n = int(input())
result = 0
for i in range(1, n + 1):
    # Calculate the number of digits in i
    temp = i
    digits = 0
    while temp > 0:
        temp //= 10
        digits += 1
    result = result * (10 ** digits) + i
print(result)
