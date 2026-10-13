class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-i-1]:
                    return False
            return True
        
        out = []
        sub = []

        def dfs(i):
            if i >= len(s):
                out.append(sub[:])
                return
            for j in range(i, len(s)):
                part = s[i:j+1]
                if is_palindrome(part):
                    sub.append(part)
                    dfs(j+1)
                    sub.pop()
        
        dfs(0)
        return out
