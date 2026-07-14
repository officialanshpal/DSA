class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # Custom GCD helper to prevent version-specific math module issues
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Memoization table: dp[(g1, g2)] -> count
        dp = {(0, 0): 1}
        
        for x in nums:
            next_dp = {}
            for (g1, g2), count in dp.items():
                # Choice 1: Don't pick x for either subsequence
                next_dp[(g1, g2)] = (next_dp.get((g1, g2), 0) + count) % MOD
                
                # Choice 2: Add x to seq1
                new_g1 = get_gcd(g1, x) if g1 != 0 else x
                next_dp[(new_g1, g2)] = (next_dp.get((new_g1, g2), 0) + count) % MOD
                
                # Choice 3: Add x to seq2
                new_g2 = get_gcd(g2, x) if g2 != 0 else x
                next_dp[(g1, new_g2)] = (next_dp.get((g1, new_g2), 0) + count) % MOD
                
            dp = next_dp
            
        # Sum up all combinations where g1 == g2 and both are non-empty (> 0)
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans
        