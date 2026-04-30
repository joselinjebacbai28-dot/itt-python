
import re

def find_indices(s, k):

    pattern = re.compile(f'(?=({k}))')
    matches = list(pattern.finditer(s))
    
    if not matches:
        print("(-1, -1)")
    else:
        for m in matches:
           
            print(f"({m.start()}, {m.start() + len(k) - 1})")

if __name__ == '__main__':
    s = input()
    k = input()
    find_indices(s, k)
