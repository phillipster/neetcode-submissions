class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest = 0;
        unordered_set<int> num_set(nums.begin(), nums.end());
        for (size_t i=0; i < nums.size(); ++i) {
            if (num_set.count(nums[i]-1) == 0) {
                int first = nums[i];
                while (num_set.count(first+1) == 1) {
                    ++first;
                }
                longest = max(longest, first-nums[i]+1);
            }
        }
        return longest;
    }
};
