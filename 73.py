
import re
import email.utils
pattern = r'^[a-z][a-z0-9\-\._]*@[a-z]+\.[a-z]{1,3}$'

n = int(input())

for _ in range(n):

    parsed = email.utils.parseaddr(input())
    
    if re.match(pattern, parsed[1], re.IGNORECASE):
   
        print(email.utils.formataddr(parsed))
