class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int maxVal = *max_element(nums.begin(), nums.end());

        // cnt[v] = how many times value v appears in nums
        vector<long long> cnt(maxVal + 1, 0);
        for (int x : nums) cnt[x]++;

        // multiples[g] = count of elements in nums divisible by g
        vector<long long> multiples(maxVal + 1, 0);
        for (int g = 1; g <= maxVal; g++) {
            long long s = 0;
            for (int m = g; m <= maxVal; m += g) {
                s += cnt[m];
            }
            multiples[g] = s;
        }

        // exact[g] = number of pairs whose gcd is EXACTLY g
        vector<long long> exact(maxVal + 2, 0);
        for (int g = maxVal; g >= 1; g--) {
            long long total_pairs = multiples[g] * (multiples[g] - 1) / 2;
            long long s = 0;
            for (int m = 2 * g; m <= maxVal; m += g) {
                s += exact[m];
            }
            exact[g] = total_pairs - s;
        }

        // prefix[g] = number of pairs with gcd <= g
        vector<long long> prefix(maxVal + 1, 0);
        for (int g = 1; g <= maxVal; g++) {
            prefix[g] = prefix[g - 1] + exact[g];
        }

        vector<int> answer;
        answer.reserve(queries.size());
        for (long long q : queries) {
            int lo = 1, hi = maxVal;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (prefix[mid] > q) {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            answer.push_back(lo);
        }

        return answer;
    }
};