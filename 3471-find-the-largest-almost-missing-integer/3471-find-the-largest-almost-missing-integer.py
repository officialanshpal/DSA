class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = {}
        n = len(nums)
        
        # Iterate over all possible subarrays of size k
        for i in range(n - k + 1):
            # Get the unique elements in the current subarray
            unique_in_subarray = set(nums[i : i + k])
            
            # Increment the occurrence count for each unique element
            for num in unique_in_subarray:
                counts[num] = counts.get(num, 0) + 1
                
        # Find the maximum number that appears in exactly one subarray
        max_almost_missing = -1
        for num, count in counts.items():
            if count == 1:
                max_almost_missing = max(max_almost_missing, num)
                
        return max_almost_missing