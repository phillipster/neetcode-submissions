class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        sub = []
        def dfs(i):
            if i >= len(nums):
                print(sub)
                curr = 0
                for num in sub:
                    curr ^= num
                res.append(curr)
            else:
                sub.append(nums[i])
                dfs(i+1)
                sub.pop()
                dfs(i+1)
        dfs(0)
        return sum(res)

            