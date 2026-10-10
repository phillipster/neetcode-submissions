class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using dp
        lowest_so_far = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price-lowest_so_far)
            lowest_so_far = min(lowest_so_far, price)
        return max_profit