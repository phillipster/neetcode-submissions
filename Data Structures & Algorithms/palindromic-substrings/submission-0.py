class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        num_palindromes = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_palindromes += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_palindromes += 1
                l -= 1
                r += 1
        return num_palindromes