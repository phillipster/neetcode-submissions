class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> n;
        for (int i = 0; i < nums.size(); ++i) {
            n.insert({nums[i], i});
        }
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (n.count(complement) > 0 && n[complement] != i) {
                return {min(i, n[complement]), max(i, n[complement])};
            }
        }
        return {0, 0};
    }
};
