import re
x = int(input())
for i in range (x):
    num = ()
    if re.findall(r'^[7-9]\d{9}$', num):
        print("YES")
    else:
        print("NO")    