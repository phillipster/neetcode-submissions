class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        cur_min = 1
        cur_max = 1
        for num in nums:
            cur_min, cur_max = min(num, num * cur_min, num * cur_max), max(num, num * cur_min, num * cur_max)
            result = max(result, cur_max)
        return result

