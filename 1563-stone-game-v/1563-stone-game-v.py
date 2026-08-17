from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        # Base case: If there is only 1 stone, the game ends immediately.
        if n == 1:
            return 0
            
        # Step 1: Build the prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
            
        # max_l[i][j] stores the max of (dp[i][k] + sum(i, k)) for k in range i to j
        max_l = [[0] * n for _ in range(n)]
        # max_r[i][j] stores the max of (dp[k][j] + sum(k, j)) for k in range i to j
        max_r = [[0] * n for _ in range(n)]
        
        res = 0
        
        # Step 2: Bottom-up DP processing intervals
        for i in range(n - 1, -1, -1):
            # Base initialization for single elements
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
            mid = i  # This pointer tracks our balance point
            
            for j in range(i + 1, n):
                target = prefix[i] + prefix[j + 1]
                
                # Move 'mid' forward as long as the left sum is <= the right sum
                while mid < j and prefix[mid + 1] * 2 <= target:
                    mid += 1
                    
                split = mid - 1
                equal = (prefix[split + 1] * 2 == target)
                
                dp_val = 0
                
                # If they are perfectly equal, Alice checks both optimal left and right choices
                if equal:
                    dp_val = max(dp_val, max_l[i][split])
                    dp_val = max(dp_val, max_r[split + 1][j])
                else:
                    # Otherwise, Alice is forced based on which sum was smaller
                    if split >= i:
                        dp_val = max(dp_val, max_l[i][split])
                    if split + 1 < j:
                        dp_val = max(dp_val, max_r[split + 2][j])
                        
                # Update our max prefix arrays for future larger intervals to use
                curr_sum = prefix[j + 1] - prefix[i]
                max_l[i][j] = max(max_l[i][j - 1], dp_val + curr_sum)
                max_r[i][j] = max(max_r[i + 1][j], dp_val + curr_sum)
                
                # If this is the full array [0 to n-1], save the answer
                if i == 0 and j == n - 1:
                    res = dp_val
                    
        return res