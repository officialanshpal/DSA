class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # Calculate the product of the digits of the current number
            digit_product = 1
            for digit in str(n):
                digit_product *= int(digit)
            
            # Check if the product is evenly divisible by t
            if digit_product % t == 0:
                return n
            
            # If not, move to the next number
            n += 1
    