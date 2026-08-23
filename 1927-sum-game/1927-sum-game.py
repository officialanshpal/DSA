class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        s1, q1 = 0, 0
        s2, q2 = 0, 0
        
        # Calculate sum and question marks for the first half
        for i in range(mid):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])
                
        # Calculate sum and question marks for the second half
        for i in range(mid, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])
                
        # If the total number of '?' is odd, Alice always wins
        if (q1 + q2) % 2 != 0:
            return True
            
        # If even, Bob wins only if he can perfectly balance the sums
        return 2 * (s1 - s2) != 9 * (q2 - q1)