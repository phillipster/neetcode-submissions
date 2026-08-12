class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int j = numbers.size()-1;
        // while (numbers[j] > target) --j;
        int i = 0;
        while (i < j) {
            int sum = numbers[i] + numbers[j];
            if (sum == target) return {++i, ++j};
            else if (sum > target) --j;
            else ++i;
        }    
        return {++i, ++j};
    }
};
