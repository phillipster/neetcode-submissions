class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub = []
        def backtrack(i):
            if len(sub) == k:
                res.append(sub[:])
            elif i > n:
                return
            else:
                sub.append(i)
                backtrack(i + 1)
                sub.pop()
                backtrack(i + 1)

        backtrack(1)
        return res
            