def prime_num(numbers):
    if(numbers == 1):
        return False
    elif (numbers == 2):
        return True
    else:
        for x in range(2, numbers):
            if( numbers % x == 0):
                return False
        return True
print(prime_num(9))                        

