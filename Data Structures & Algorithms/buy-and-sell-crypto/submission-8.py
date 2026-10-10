class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using dp
        n = len(prices)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            if prices[i] > dp[i+1]:
                dp[i] = prices[i]
            else:
                dp[i] = dp[i+1]
        max_profit = 0
        for i in range(n-1):
            max_profit = max(max_profit, dp[i+1]-prices[i])
        return max_profit