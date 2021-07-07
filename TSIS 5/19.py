import glob
ch_list = []
files_list = glob.glob("*.txt")
for file_elem in files_list:
   with open(file_elem, "r") as f:
       ch_list.append(f.read())
print(ch_list)