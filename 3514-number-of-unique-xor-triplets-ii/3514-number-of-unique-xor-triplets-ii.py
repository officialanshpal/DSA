class Solution:
    def uniqueXorTriplets(self, nums):
        unique = list(set(nums))
        m = len(unique)
        
        # Step 1: all pairwise XORs (with repetition, i.e., a^a included)
        pair_xor = set()
        for i in range(m):
            for j in range(i, m):
                pair_xor.add(unique[i] ^ unique[j])
        
        # Step 2: XOR each pairwise result with every value to get triplet XORs
        triple_xor = set()
        for p in pair_xor:
            for c in unique:
                triple_xor.add(p ^ c)
        
        return len(triple_xor)