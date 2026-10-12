class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0,0,0]
        for i in range(2, n+1):
            dp[2] = min(dp[1] + cost[i-1], dp[0] + cost[i-2])
            dp[1], dp[0] = dp[2], dp[1]
        return dp[-1]