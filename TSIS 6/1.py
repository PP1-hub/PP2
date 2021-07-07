def maximum_three(x, y, z):
    if( x >= y ) & ( x >= z):
        max = x
    elif (y >= z) & (y >= z):
        max = y  
    else:
        max = z
          
    return max 
print(maximum_three(6, 46, -70))
