x = set(map(int, input().split()))
y = set(map(int, input().split()))
print(*sorted(x & y))