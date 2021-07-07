def text_string(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for x in s:
        if x.isupper():
           d["UPPER_CASE"]+=1
        elif x.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print("No. of Upper case characters : ", d["UPPER_CASE"])    
    print("No. of Lower case Characters : ", d["LOWER_CASE"])    

text_string='The quick Brown Fox'

  
