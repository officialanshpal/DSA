class Solution:
    def maxProduct(self, n):
        # Convert the number to a string and sort it in descending order
        digits = sorted(str(n), reverse=True)
        
        # Multiply the two largest digits
        return int(digits[0]) * int(digits[1])