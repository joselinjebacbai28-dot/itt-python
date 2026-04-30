
import re

n = int(input())
pattern = r'(?<=[: ])#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b'

for _ in range(n):
    line = input()

    matches = re.findall(pattern, line)
    for m in matches:
        print(f"#{m}")
