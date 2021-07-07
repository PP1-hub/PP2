x = set()
y = set()
a, b =[int(i) for i in input().split()]
for i in range(a):
    x.add(int(input()))
for i in range(b):
    y.add(int(input()))
print(len(x & y))
print(*sorted(x & y))
print(len(x - y))
print(*sorted(x - y))
print(len(y - x))
print(*sorted(y-x))
