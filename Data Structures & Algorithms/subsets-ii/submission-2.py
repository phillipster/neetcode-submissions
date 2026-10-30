class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        curr = []

        def dfs(i):
            if i >= n:
                temp = tuple(sorted(curr))
                if temp not in res:
                    res.add(temp)
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)

        dfs(0)
        return list(list(item) for item in res)