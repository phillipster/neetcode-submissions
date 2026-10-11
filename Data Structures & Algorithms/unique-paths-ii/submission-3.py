class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        og = obstacleGrid
        if og[0][0] == 1:
            return 0
        m, n = len(og), len(og[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if og[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for row in dp:
            print(row)
        return dp[-1][-1]
