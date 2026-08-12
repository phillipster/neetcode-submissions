class Solution {
public:
    bool isPalindrome(string s) {
        size_t i = 0, j = s.size()-1;
        while (i < j) { 
            if (!(isalnum(s[i]) && isalnum(s[j]))) {
                if (!(isalnum(s[i]))) ++i;
                if (!(isalnum(s[j]))) --j;;
            } else {
                if (tolower(s[i]) != tolower(s[j])) return false;
                ++i;
                --j;
            }
        }
        return true;
    }
};
