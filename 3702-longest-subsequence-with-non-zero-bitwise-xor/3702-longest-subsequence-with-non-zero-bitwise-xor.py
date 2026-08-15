class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        n = len(nums)
        
        # Case 1: If the XOR of the entire array is non-zero, the whole array is the answer.
        if total_xor != 0:
            return n
        
        # Case 2: The total XOR is 0.
        # If all elements are 0, it's impossible to get a non-zero XOR subsequence.
        if all(num == 0 for num in nums):
            return 0
            
        # Case 3: Total XOR is 0, but there is at least one non-zero element.
        # Removing that single non-zero element guarantees the remaining XOR is non-zero.
        return n - 1