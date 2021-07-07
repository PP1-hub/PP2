class Solution(object):
    def subtractProductAndSum(self, n):
        num_list=[int(i) for i in str(n)]
        sum_list=sum(num_list)
        
        product_list = 1
        
        for i in num_list:
            product_list *= i
        return product_list - sum_list