class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # Array to store the frequency of stones with modulo 0, 1, and 2
        counts = [0, 0, 0]
        
        for stone in stones:
            counts[stone % 3] += 1
            
        # If the count of modulo 0 stones is even
        if counts[0] % 2 == 0:
            return counts[1] > 0 and counts[2] > 0
            
        # If the count of modulo 0 stones is odd
        else:
            return abs(counts[1] - counts[2]) > 2