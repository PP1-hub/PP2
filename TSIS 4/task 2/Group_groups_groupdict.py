import re
x = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(x.group(1) if x else -1)