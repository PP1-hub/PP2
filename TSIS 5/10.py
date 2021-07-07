from collections import Counter
f = open("text.txt")
print(Counter(f.read().split()))


