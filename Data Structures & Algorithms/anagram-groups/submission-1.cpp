class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (const string& s : strs) {
            string temp = s;
            sort(temp.begin(), temp.end());
            groups[temp].push_back(s);
        }
        vector<vector<string>> out;
        for (const auto& it : groups) {
            out.push_back(it.second);
        }
        return out;
    }
};
