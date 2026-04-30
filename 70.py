
import re

for _ in range(int(input())):
    s = input()
    try:
  
        is_float = float(s)
        
        if '.' in s:
            print(True)
        else:
            print(False)
            
    except ValueError:
        print(False)
