class Solution(object):
    def findGCD(self, nums):
        small = min(nums)
        large = max(nums)
        
        # Euclid's algorithm
        while small:
            large, small = small, large % small
            
        return large