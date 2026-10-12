class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0] if len(nums) == 1 else 0
        n = len(nums)
        def r(arr):
            dp = [0] * (n+2)
            for i in range(n-1):
                dp[i+2] = max(dp[i+1], dp[i] + arr[i])
            return dp[n]
        return max(r(nums[:n]), r(nums[1:]))