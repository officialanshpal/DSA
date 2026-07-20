class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        # Initialize a new grid of the same dimensions
        ans = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Calculate old 1D index
                old_idx = r * n + c
                
                # Calculate new 1D index after k shifts
                new_idx = (old_idx + k) % total
                
                # Convert 1D index back to 2D coordinates
                new_r = new_idx // n
                new_c = new_idx % n
                
                ans[new_r][new_c] = grid[r][c]
                
        return ans