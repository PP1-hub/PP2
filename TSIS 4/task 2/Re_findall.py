import re
x = input()
n = re.findall(r"[^aeiou]([aeiouAEIOU]{2,})(?=[^aeiou])", x)
if n:
    for i in n:
        print(i)
else:
    print(-1) 