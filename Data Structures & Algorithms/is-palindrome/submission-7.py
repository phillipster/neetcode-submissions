class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = [c for c in s if c.isalnum()]
        # print(t)
        for i in range(len(t)//2):
            if t[i] != t[len(t)-1-i]:
                return False
        return True