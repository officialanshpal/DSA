class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Suffix sum array to quickly calculate remaining stones
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, m):
            # If the current player can take all the remaining piles, take them all
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            max_stones = 0
            # Try all possible valid moves X (from 1 to 2m)
            for x in range(1, 2 * m + 1):
                # Stones current player gets = (Total remaining stones) - (Stones next player gets)
                current_stones = suffix_sum[i] - dp(i + x, max(m, x))
                max_stones = max(max_stones, current_stones)
                
            return max_stones
        
        # Start the game from index 0 with M = 1
        return dp(0, 1)