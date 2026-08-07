class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Extract prime factors 2, 3, 5, 7 from t
        factors = [0] * 4  # stores counts of [2, 3, 5, 7]
        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                factors[i] += 1
                t //= p
        
        # If t has other prime factors (> 7), no solution is possible
        if t > 1:
            return "-1"
            
        # Helper to find the minimum string required to satisfy factor counts
        def get_min_suffix(f2, f3, f5, f7):
            # We want to greedily pack factors into larger digits (9, 8, 6, 4)
            # to minimize the number of digits needed
            n9 = max(0, f3 // 2)
            f3 %= 2
            
            n8 = max(0, f2 // 3)
            f2 %= 3
            
            n7 = max(0, f7)
            n5 = max(0, f5)
            
            # Combine remaining 2s and 3s
            n6 = 0
            n4 = 0
            n3 = max(0, f3)
            n2 = max(0, f2)
            
            if n3 == 1 and n2 > 0:
                n6 = 1
                n3 = 0
                n2 -= 1
            if n2 == 2:
                n4 = 1
                n2 = 0
                
            res = (['2'] * n2 + ['3'] * n3 + ['4'] * n4 + 
                   ['5'] * n5 + ['6'] * n6 + ['7'] * n7 + 
                   ['8'] * n8 + ['9'] * n9)
            return "".join(res)

        # Sanitize num: replace the first '0' and all subsequent digits with '1'
        s = list(num)
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                for j in range(i, n):
                    s[j] = '1'
                break

        # Count current prime factors present in the sanitized string
        cur_factors = [0] * 4
        for char in s:
            d = int(char)
            for i, p in enumerate([2, 3, 5, 7]):
                while d % p == 0 and d > 0:
                    cur_factors[i] += 1
                    d //= p

        # Check if the sanitized string itself is already valid
        if all(cur_factors[i] >= factors[i] for i in range(4)):
            return "".join(s)

        # Step 3: Backtrack from right to left to find an increment point
        for i in range(n - 1, -1, -1):
            # Remove current digit's factors from prefix tracking
            d = int(s[i])
            temp_d = d
            for k, p in enumerate([2, 3, 5, 7]):
                while temp_d % p == 0 and temp_d > 0:
                    cur_factors[k] -= 1
                    temp_d //= p
            
            # Try to increment the digit at position i
            for next_digit in range(d + 1, 10):
                # Calculate factors contributed by next_digit
                next_f = [0] * 4
                temp_nd = next_digit
                for k, p in enumerate([2, 3, 5, 7]):
                    while temp_nd % p == 0:
                        next_f[k] += 1
                        temp_nd //= p
                
                # Check required factors for the remaining suffix positions
                req = [max(0, factors[k] - cur_factors[k] - next_f[k]) for k in range(4)]
                min_suff = get_min_suffix(*req)
                rem_len = n - 1 - i
                
                # If the required minimum suffix fits in the remaining length
                if len(min_suff) <= rem_len:
                    # Pad with '1's to match the exact remaining length
                    pad_ones = '1' * (rem_len - len(min_suff))
                    return "".join(s[:i]) + str(next_digit) + pad_ones + min_suff

        # Step 4: If no solution exists with length n, increase length to n + 1
        req = [max(0, factors[k]) for k in range(4)]
        min_suff = get_min_suffix(*req)
        total_len = max(n + 1, len(min_suff))
        return '1' * (total_len - len(min_suff)) + min_suff
