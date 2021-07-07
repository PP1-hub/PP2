array = []
f = open("text.txt")
for line in f:
    array.append(line)
print(*array)
print(type(array))