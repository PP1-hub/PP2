def multiply_list(numbers):
    counter = 1
    for x in numbers:
        counter *= x
    return counter 
print(multiply_list((8, 2, 3, -1, 7)))        