class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(arr):
            if len(arr) == 0:
                return False
            s = 0
            for i in range(len(arr)):
                if arr[i] == '(':
                    s += 1
                else:
                    if not s:
                        return False
                    s -= 1
            return s == 0

        out = set()
        sub = []
        def dfs(i):
            if i > n*2:
                return
            if len(sub) == n*2 and is_valid(sub):
                out.add(''.join(sub[:]))
            sub.append("(")
            dfs(i + 1)
            sub.pop()
            sub.append(")")
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)
        dfs(0)
        return list(out)