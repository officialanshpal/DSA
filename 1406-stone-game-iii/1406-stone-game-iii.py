class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] will store the max score difference a player can get starting at index i
        # We append a 0 at the end to handle the base case where no stones are left (index n)
        dp = [float('-inf')] * n + [0]
        
        # Work backwards from the end of the array
        for i in range(n - 1, -1, -1):
            take_sum = 0
            
            # The player can take 1, 2, or 3 stones
            for j in range(3):
                if i + j < n:
                    take_sum += stoneValue[i + j]
                    # We want to maximize our stones minus the best the opponent can do next
                    dp[i] = max(dp[i], take_sum - dp[i + j + 1])
                    
        # dp[0] now contains the max score difference Alice can achieve over Bob
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"