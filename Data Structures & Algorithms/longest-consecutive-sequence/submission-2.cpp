class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest_streak = 0;
        unordered_set<int> n(nums.begin(), nums.end());
        for (size_t i = 0; i < nums.size(); ++i) {
            if (n.count(nums[i]-1)) continue;
            int cur_streak = 1;
            int cur = nums[i];
            while (n.count(++cur)) ++cur_streak;
            if (cur_streak > longest_streak) longest_streak = cur_streak;
        }
        return longest_streak;
    }
};
