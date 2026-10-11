class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i+1][j+1] = grid[i][j] + dp[i+1][j]
                elif j == 0:
                    dp[i+1][j+1] = grid[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])
        for row in dp:
            print(row)
        return dp[-1][-1]