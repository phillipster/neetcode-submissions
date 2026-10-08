class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        chars = set()
        l = r = 0
        length = 1
        while r < n:
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            length = max(length, r-l)
        return length