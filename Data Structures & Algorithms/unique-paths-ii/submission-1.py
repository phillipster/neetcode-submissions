class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        og = obstacleGrid
        if og[0][0] == 1:
            return 0
        m, n = len(og), len(og[0])
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            if og[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if og[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if og[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for row in dp:
            print(row)
        return dp[-1][-1]
