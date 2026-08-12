class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> frequencies;
        for (int i : nums) {
            if (frequencies.count(i) == 0) {
                frequencies.insert(i);
            } else {
                return true;
            }
        }
        return false;
    }
};