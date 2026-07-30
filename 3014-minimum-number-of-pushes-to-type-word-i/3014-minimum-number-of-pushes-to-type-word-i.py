class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        freqs = sorted(Counter(word).values(), reverse=True)
        
        total = 0
        for i, f in enumerate(freqs):
            total += (i // 8 + 1) * f
            
        return total