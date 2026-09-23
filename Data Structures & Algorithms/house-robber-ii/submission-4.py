class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_help(nums: List[int]):
            rob1, rob2 = 0, 0

            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        if len(nums) <= 3:
            return max(nums)
        return max(rob_help(nums[1:]), rob_help(nums[:-1]))