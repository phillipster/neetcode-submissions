class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                out.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return out