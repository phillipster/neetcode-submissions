class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> n;
        for (size_t i = 0; i < nums.size(); ++i) {
            n[nums[i]] = i;
        }
        for (size_t i = 0; i < nums.size(); ++i) {
            int complement = target-nums[i];
            if (n.count(complement) == 1 && i != n[complement]) {
                return {i, n[complement]};
            }
        }
        return {-1, -1};
    }
};
