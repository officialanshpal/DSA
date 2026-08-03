class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j] will store the max relative score a player can get from piles[i] to piles[j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: when there is only one pile, the player takes it
        for i in range(n):
            dp[i][i] = piles[i]
            
        # Build the DP table for lengths 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # The player can choose either the left pile (piles[i]) or the right pile (piles[j])
                # They want to maximize their score minus the opponent's score from the remaining piles
                left_choice = piles[i] - dp[i + 1][j]
                right_choice = piles[j] - dp[i][j - 1]
                dp[i][j] = max(left_choice, right_choice)
                
        # If the max relative score from the whole array is > 0, Alice wins
        return dp[0][n - 1] > 0