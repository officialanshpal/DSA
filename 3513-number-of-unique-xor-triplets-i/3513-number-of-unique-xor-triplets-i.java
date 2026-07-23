class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        
        // Handle small constraints explicitly
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // For n >= 3, find the most significant bit (MSB)
        int msb = 0;
        while ((1 << (msb + 1)) <= n) {
            msb++;
        }
        
        // We can generate all values up to 2^(msb + 1) - 1
        return 1 << (msb + 1);
    }
}