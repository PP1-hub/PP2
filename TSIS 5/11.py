import os
size = os.stat("text.txt")
print(size.st_size)