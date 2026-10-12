class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        longest = s[0]

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            longest = longest if len(longest) > r-l-1 else s[l+1:r]
        
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            longest = longest if len(longest) > r-l-1 else s[l+1:r]
        return longest