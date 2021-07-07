class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        highest = 0
        
        for x in gain:
            current +=x
            highest = max(current, highest)
        return highest