
import re

pattern = r"([a-zA-Z0-9])\1"

if m:
    print(m.group(1))
else:
    print("-1")
