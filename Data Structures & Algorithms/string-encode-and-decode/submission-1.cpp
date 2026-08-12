class Solution {
public:

    string encode(vector<string>& strs) {
        string out;
        for (const string& s : strs) {
            out += to_string(s.size()) + '#' + s;
        }
        return out;
    }

    vector<string> decode(string s) {
        vector<string> out;
        size_t i = 0;
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            i = j + 1;
            j = i + length;
            out.push_back(s.substr(i, length));
            i = j;
        }
        return out;
    }
};
