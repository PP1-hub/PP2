f = open("text2.txt", "w")
fruits = ["orange", "kiwi", "pomegranate"]
for i in fruits:
    f.write("%s\n" % fruits)