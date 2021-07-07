def perfect_num(numbers):
    count = 0
    for x in range(1, numbers):
        if numbers % x ==0:
            count +=x
    return count == numbers
print(perfect_num(6))            
