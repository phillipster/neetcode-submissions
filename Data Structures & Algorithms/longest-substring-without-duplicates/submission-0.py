class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        count = 1
        letters = set()
        letters.add(s[0])
        l, r = 0, 1
        while r < len(s):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            count = max(count, r-l+1)
            letters.add(s[r])
            r += 1
        return count
