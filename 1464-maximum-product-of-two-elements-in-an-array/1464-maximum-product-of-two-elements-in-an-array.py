class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        max2 = 0
        
        for num in nums:
            if num > max1:
                # The old maximum becomes the second maximum
                max2 = max1
                max1 = num
            elif num > max2:
                # If it's not greater than max1, check if it's greater than max2
                max2 = num
                
        return (max1 - 1) * (max2 - 1)