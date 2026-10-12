class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[-1] = True
        for i in range(n-1, -1, -1):
            if nums[i] + i >= n-1:
                dp[i] = True
            else:
                for j in range(nums[i]):
                    if dp[i+j] == True:
                        dp[i] = True
                        break
                else:
                    dp[i] = dp[i+nums[i]]
        print(dp)
        return dp[0]