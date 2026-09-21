class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0]*26
        max_len = 0
        l = r = 0
        while l <= r < len(s):
            slot = ord(s[r])-ord('A')
            counts[slot] += 1
            while r-l+1 - max(counts) > k:
                counts[ord(s[l])-ord('A')] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len
            