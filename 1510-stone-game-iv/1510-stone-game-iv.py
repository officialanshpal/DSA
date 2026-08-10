class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] represents if the current player can win with i stones remaining
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            # Check all possible valid square numbers we can remove
            while k * k <= i:
                # If removing k*k stones leaves the opponent in a losing state, 
                # then the current state 'i' is a winning state.
                if not dp[i - k * k]:
                    dp[i] = True
                    break # We found a winning strategy, no need to check further
                k += 1
                
        # Return the result for n stones
        return dp[n]