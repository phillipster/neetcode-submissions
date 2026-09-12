class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float('inf')
        best_profit_so_far = 0
        for num in prices:
            min_price_so_far = min(num, min_price_so_far)
            best_profit_so_far = max(best_profit_so_far, num-min_price_so_far)
        return best_profit_so_far