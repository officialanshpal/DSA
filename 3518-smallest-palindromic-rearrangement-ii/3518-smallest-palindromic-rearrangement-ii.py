import math
from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Step 1: Count character frequencies and determine the available pool for the first half
        counts = Counter(s)
        half_counts = {}
        odd_char = ""
        
        for char, count in counts.items():
            half_counts[char] = count // 2
            if count % 2 != 0:
                odd_char = char
                
        L = len(s) // 2
        
        # Step 2: Calculate the total possible unique palindromic permutations
        total_perms = math.factorial(L)
        for count in half_counts.values():
            total_perms //= math.factorial(count)
            
        if k > total_perms:
            return ""
            
        ans = []
        current_perms = total_perms
        
        # Step 3: Construct the first half lexicographically
        for i in range(L):
            remaining_len = L - i
            
            # Try placing each character from 'a' to 'z'
            for char_code in range(26):
                char = chr(ord('a') + char_code)
                
                if half_counts.get(char, 0) > 0:
                    count = half_counts[char]
                    
                    # Calculate permutations if we select 'char' for this position
                    perms = current_perms * count // remaining_len
                    
                    if k <= perms:
                        # The k-th permutation falls within this branch
                        ans.append(char)
                        half_counts[char] -= 1
                        current_perms = perms
                        break
                    else:
                        # Skip this branch and reduce k
                        k -= perms
                        
        # Step 4: Mirror the first half to form the final palindrome
        first_half = "".join(ans)
        return first_half + odd_char + first_half[::-1]