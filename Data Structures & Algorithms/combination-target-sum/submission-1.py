class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def dfs(i, total):
            if i > len(nums)-1 or total > target:
                return
            if total == target:
                res.append(sub[:])
                return
            sub.append(nums[i])
            dfs(i, total + nums[i])
            sub.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res