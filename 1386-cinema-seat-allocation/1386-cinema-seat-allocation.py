import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Dictionary to store a bitmask of reserved seats for each row
        row_masks = collections.defaultdict(int)
        
        for row, seat in reservedSeats:
            # We only care about seats 2 through 9
            if 2 <= seat <= 9:
                # Map seat 2 to bit 0, seat 3 to bit 1, ..., seat 9 to bit 7
                row_masks[row] |= (1 << (seat - 2))
                
        # Start by assuming all rows are empty (2 groups per row)
        max_groups = 2 * n
        
        # Bitmasks for our three valid 4-seat blocks
        left_mask = 0b00001111   # Represents seats 2, 3, 4, 5
        mid_mask = 0b00111100    # Represents seats 4, 5, 6, 7
        right_mask = 0b11110000  # Represents seats 6, 7, 8, 9
        
        for row, mask in row_masks.items():
            # Remove the 2 groups we initially assumed for this row
            max_groups -= 2 
            
            # Check which blocks are available (bitwise AND evaluates to 0 if no overlap)
            if (mask & left_mask) == 0 and (mask & right_mask) == 0:
                max_groups += 2
            elif (mask & left_mask) == 0 or (mask & right_mask) == 0 or (mask & mid_mask) == 0:
                max_groups += 1
                
        return max_groups