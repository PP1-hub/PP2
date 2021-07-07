def func_1(x):
    def func_2(y):
        return x * y
    return func_2
func= func_1(4)
print(func(4))