
import re

def change(match):
    if match.group(0) == '&&':
        return 'and'
    else:
        return 'or'

n = int(input())

for _ in range(n):
    line = input()
    
    line = re.sub(r"(?<= )(&&)(?= )", "and", line)
    line = re.sub(r"(?<= )(\|\|)(?= )", "or", line)
    print(line)
