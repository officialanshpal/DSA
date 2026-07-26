class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        # Option 1: Product of the 3 largest elements
        prod1 = nums[-1] * nums[-2] * nums[-3]
        
        # Option 2: Product of 2 smallest (most negative) and the largest element
        prod2 = nums[0] * nums[1] * nums[-1]
        
        return max(prod1, prod2)