class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        chars = [False]*128
        l = r = 0
        length = 0
        while r < n:
            if not chars[ord(s[r])]:
                chars[ord(s[r])] = True
                r += 1
            else:
                while chars[ord(s[r])]:
                    chars[ord(s[l])] = False
                    l += 1
            length = max(length, r-l)
        return length