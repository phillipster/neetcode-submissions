class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        subset = []
        def dfs(i, total):
            if i > len(nums)-1 or total > target:
                return
            if sum(subset) == target:
                out.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()
            dfs(i+1, total)
        
        dfs(0, 0)
        return out
            