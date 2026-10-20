class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        n = len(height)
        left = [0] * n
        right = [height[-1]] * n
        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        dp = [0] * n
        for i in range(n):
            dp[i] = max(min(left[i], right[i])-height[i], 0)
        return sum(dp)