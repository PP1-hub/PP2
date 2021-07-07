def even_num(x):
    a = []
    for n in x:
        if n % 2 ==0:
            a.append(n)
    return a         

print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))        
