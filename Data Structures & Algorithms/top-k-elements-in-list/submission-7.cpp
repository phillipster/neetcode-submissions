class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int n : nums) {
            ++freq[n];
        }
        vector<pair<int, int>> swapped;
        for (const auto& [key, value] : freq) {
            swapped.push_back({value, key});
        }
        std::ranges::sort(
            swapped, [](const pair<int, int>& a, const pair<int, int>& b) {
                return a.first > b.first;
            }
        );
        vector<int> out(k);
        for (int i = 0; i < k; ++i) {
            out[i] = swapped[i].second;
        }
        return out;
    }

};
