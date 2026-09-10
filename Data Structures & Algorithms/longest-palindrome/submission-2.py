class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        m = {}
        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
                if m[c] % 2 == 0:
                    total += 2
        for val in m.values():
            if val % 2 == 1:
                total += 1
                break
        return total