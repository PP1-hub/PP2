f = open("text.txt").readlines()
print([s.rstrip('\n') for s in f])