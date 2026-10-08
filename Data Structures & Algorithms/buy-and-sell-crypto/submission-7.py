class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        maxSoFar = 0
        while r < n:
            curr_prof = prices[r]-prices[l]
            if curr_prof > maxSoFar:
                maxSoFar = curr_prof
            elif prices[r] < prices[l]:
                l = r
            r += 1
        return maxSoFar