class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = set()
        sub = []
        def dfs(i, total):
            if total == target:
                output.add(tuple(sub[:]))
            if i >= len(nums) or total > target:
                return
            sub.append(nums[i])
            dfs(i+1, total + nums[i])
            sub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i+1, total)
        dfs(0, 0)
        return [list(t) for t in output]
            