class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string has 1 way
        dp[1] = 1  # First character is guaranteed non-zero

        for i in range(2, n + 1):
            one_digit = int(s[i-1:i])
            two_digit = int(s[i-2:i])

            # Take single digit if it's 1-9
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]

            # Take two digits if it's 10-26
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[-1]