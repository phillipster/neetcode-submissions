class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp1, dp0 = 0, 0
        for i in range(2, n+1):
            dp1, dp0 = min(dp1 + cost[i-1], dp0 + cost[i-2]), dp1
        return dp1