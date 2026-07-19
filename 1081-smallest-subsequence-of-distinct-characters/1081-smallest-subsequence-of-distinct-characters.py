class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Find the last occurrence index of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for idx, char in enumerate(s):
            # If the character is already in our result subsequence, skip it
            if char in seen:
                continue
                
            # Maintain a monotonic increasing order in the stack where possible
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > idx:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character to the stack and seen set
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)