class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [nums[0]] * len(nums)
        right_prod = [nums[len(nums)-1]] * len(nums)
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i]
        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i]
        out = [0] * len(nums)
        for i in range(1, len(nums)-1):
            out[i] = left_prod[i-1] * right_prod[i+1]
        out[0] = right_prod[1]
        out[len(out)-1] = left_prod[len(left_prod)-2]
        return out