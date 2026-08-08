class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # last[j] stores the largest index in word1 that matches word2[j] 
        # greedily from the suffix end.
        last = [-1] * m
        
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1
            
        ans = []
        j = 0
        can_skip = True # Tracks if our 1 allowed mismatch change is available
        
        # Greedily match from the beginning to ensure lexicographically smallest indices
        for i in range(n):
            if j == m:
                break
                
            # Case 1: Exact character match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
                
            # Case 2: Mismatch, try using our single allowed change/skip
            elif can_skip and (j == m - 1 or i < last[j + 1]):
                can_skip = False # Consume our single free change
                ans.append(i)
                j += 1
                
        return ans if len(ans) == m else []
