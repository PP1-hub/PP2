class Solution(object):
    def numIdenticalPairs(self, nums):
        n = 0
        for count, value in enumerate(nums):
            for x in nums[count+1:]:
                if x == value:
                    n+=1
        return n  