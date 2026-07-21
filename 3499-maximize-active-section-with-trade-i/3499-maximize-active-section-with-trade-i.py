class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        # Augment s with '1' at both ends
        t = "1" + s + "1"
        
        # Group contiguous blocks of same characters
        # e.g., t = "101001" -> [('1', 1), ('0', 1), ('1', 1), ('0', 2), ('1', 1)]
        blocks = []
        for char in t:
            if blocks and blocks[-1][0] == char:
                blocks[-1][1] += 1
            else:
                blocks.append([char, 1])
        
        max_delta = 0
        
        # A valid '1' block to trade must be strictly inside t
        # i.e., blocks[i] is '1', with blocks[i-1] as '0' and blocks[i+1] as '0'
        for i in range(1, len(blocks) - 1):
            if blocks[i][0] == '1':
                # Check if it has '0' blocks on both sides
                if blocks[i-1][0] == '0' and blocks[i+1][0] == '0':
                    left_zero_len = blocks[i-1][1]
                    right_zero_len = blocks[i+1][1]
                    
                    delta = left_zero_len + right_zero_len
                    max_delta = max(max_delta, delta)
                    
        return initial_ones + max_delta