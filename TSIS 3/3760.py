x = int(input())
map={}
for i in range(x):
    a,b=input().split()
    map[a]=b
    map[b]=a
z = input()
print(map[z])  