class Solution(object):
    # Custom GCD function compatible with Python 2
    def get_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefixGcd = [0] * n
        current_max = 0
        
        # Step 1: Construct prefixGcd array using custom GCD
        for i in range(n):
            current_max = max(current_max, nums[i])
            prefixGcd[i] = self.get_gcd(nums[i], current_max)
            
        # Step 2: Sort prefixGcd in non-decreasing order
        prefixGcd.sort()
        
        # Step 3 & 4: Form pairs and compute the sum of their GCDs
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            # Take the smallest (left) and largest (right) unpaired elements
            total_sum += self.get_gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum
        