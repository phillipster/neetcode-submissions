class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Create a 2D DP array initialized with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the table in a bottom-up manner
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The bottom-right corner contains the final answer
        return dp[m][n]
            