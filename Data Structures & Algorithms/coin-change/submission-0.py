from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            

            min_coins = inf
            for c in coins:
                if i - c >= 0:
                    min_coins = min(min_coins, 1 + dfs(i - c))
            memo[i] = min_coins

            return min_coins
        
        min_coins = dfs(amount)
        
        return min_coins if min_coins < inf else -1

            