def count_words(file):
   with open(file) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("text.txt"))