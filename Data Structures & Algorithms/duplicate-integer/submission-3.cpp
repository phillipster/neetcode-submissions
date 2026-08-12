class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> present;
        for (int num : nums) {
            if (present.contains(num)) {
                return true;
            }
            present.insert(num);
        }
        return false;
    }
};