import re
n = int(input())
for i in range(n):
    a = input()
    print(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$', a)))