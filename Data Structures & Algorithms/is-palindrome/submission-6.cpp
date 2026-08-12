class Solution {
public:
    bool isPalindrome(string s) {
        size_t i = 0, j = s.size()-1;
        while (i < j) {
            char c1 = s[i], c2 = s[j];
            if (!isalnum(c1) || !isalnum(c2)) {
                if (!isalnum(c1)) {
                    ++i;
                }
                if (!isalnum(c2)) {
                    --j;
                }
            } else {
                c1 = tolower(c1);
                c2 = tolower(c2);
                if (c1 != c2) return false;
                ++i;
                --j;
            }
        }
        return true;
    }
};
