x = list(map(int, input().split()))
a = []
for i in x:
    if i != 0:
        print(i, end=' ')
    else:
        a.append(i)
for i in a:
    print(i, end=' ')            