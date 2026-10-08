class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if 0 <= len(prices) <= 1:
            return 0
        n = len(prices)
        l, r = 0, 1
        maxSoFar = 0
        while r < n:
            if prices[r] > prices[l]:
                maxSoFar = max(prices[r]-prices[l], maxSoFar)
            elif prices[r] < prices[l]:
                l = r
            r += 1
        return maxSoFar