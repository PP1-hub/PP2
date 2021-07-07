def palindrome(str):
    if len(str) < 1:
        return True
    else:
        if str[0] == str[-1]:
            return palindrome(str[1:-1])
        else:
            return False
a=str(input("aza"))
   
print(palindrome('aza'))    
