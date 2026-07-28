class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Count the frequency of each character
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
            
        left_half = []
        middle = ""
        
        # Step 2 & 3: Iterate through characters in alphabetical order
        for char in sorted(char_counts.keys()):
            count = char_counts[char]
            
            # If the count is odd, this character goes in the middle
            if count % 2 != 0:
                middle = char
                
            # Append half of the occurrences to the left half
            left_half.append(char * (count // 2))
            
        # Step 4: Combine the left half, middle, and mirrored right half
        left_str = "".join(left_half)
        return left_str + middle + left_str[::-1]