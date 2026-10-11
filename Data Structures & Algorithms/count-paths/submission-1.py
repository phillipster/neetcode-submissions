class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*(n+1) for _ in range(m+1)]
        for row in dp:
            print(row)
        print("===================")
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        for row in dp:
            print(row)
        return dp[-2][-2]