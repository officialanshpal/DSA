class Solution:
    def sequentialDigits(self, low, high):
        result = []
        digits = "123456789"
        
        # Length of the numbers to generate
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
        return result