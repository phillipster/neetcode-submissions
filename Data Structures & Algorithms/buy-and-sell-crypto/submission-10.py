class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        prev_min = float('inf')
        for val in prices:
            best_profit = max(best_profit, val-prev_min)
            prev_min = min(prev_min, val)
        return best_profit