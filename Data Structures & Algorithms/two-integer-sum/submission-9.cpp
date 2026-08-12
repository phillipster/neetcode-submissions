class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            m[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); ++i) {
            int comp = target-nums[i];
            if (m.contains(comp) && m[comp] != i) {
                return vector<int> {min(i, m[comp]), max(i, m[comp])};
            }
        }
    }
};
