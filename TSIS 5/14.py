file1= open('text.txt')
file2= open('text2.txt')
for i,j in zip(file1, file2):
    print(i+j)
