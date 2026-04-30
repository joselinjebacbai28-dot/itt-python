
from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    char_counts = Counter(sorted(s)).most_common(3)
    
    for char, count in char_counts:
        print(f"{char} {count}")
