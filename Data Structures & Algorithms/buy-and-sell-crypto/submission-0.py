class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if 0 <= len(prices) <= 1:
            return 0
        i, j = 0, 1
        largest_in_future = [0] * len(prices)
        for i in range(len(prices)-2, -1, -1):
            largest_in_future[i] = max(largest_in_future[i+1], prices[i+1])
        cur_max = 0
        for i in range(len(prices)):
            cur_max = max(cur_max, largest_in_future[i]-prices[i])
        return cur_max