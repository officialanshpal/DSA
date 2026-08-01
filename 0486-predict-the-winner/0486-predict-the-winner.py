class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp array to store the maximum score difference for the current subarray length
        dp = nums[:] 
        
        # Build the DP table for subarray lengths from 2 up to n
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                # The current player takes either the left or the right element,
                # minus the optimal score difference the opponent will get from the remainder.
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])
                
        # If the max score difference for the entire array is >= 0, Player 1 wins
        return dp[0] >= 0