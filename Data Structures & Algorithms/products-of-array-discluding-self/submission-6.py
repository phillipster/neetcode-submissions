class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [nums[0]] * n
        right_prod = [nums[-1]]* n
        for i in range(1, n):
            left_prod[i] = nums[i] * left_prod[i-1]
        for i in range(n-2, -1, -1):
            right_prod[i] = nums[i] * right_prod[i+1]
        out = [right_prod[1]] + [0]*(n-2) + [left_prod[-2]]
        for i in range(1, n-1):
            out[i] = left_prod[i-1] * right_prod[i+1]
        return out
