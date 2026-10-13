class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        sub = []

        def dfs(i):
            if i > len(digits):
                return
            if i == len(digits):
                res.append(''.join(sub))
                return
            for c in m[digits[i]]:
                sub.append(c)
                dfs(i+1)
                sub.pop()
        
        dfs(0)
        return res
        