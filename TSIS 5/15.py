import random
f = open("text.txt").read().splitlines()
print(random.choice(f))