class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;
        for (char c : s) {
            if (s_map.count(c) == 0) {
                s_map[c] = 1;
            } else {
                ++s_map[c];
            }
        }
        for (char c : t) {
            if (t_map.count(c) == 0) {
                t_map[c] = 1;
            } else {
                ++t_map[c];
            }
        }
        return s_map == t_map;
    }
};
