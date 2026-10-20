class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        left, right = 0, 1
        seen = set([s[left]])
        longest = 1
        while right < n:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right-left+1)
            right += 1
        return longest
        