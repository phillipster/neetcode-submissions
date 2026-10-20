class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        while left < right:
            print(s[left], s[right])
            if not (s[left].isalnum() and s[right].isalnum()):
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left+1, right-1
        return True