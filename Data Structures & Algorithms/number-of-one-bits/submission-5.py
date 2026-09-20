class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for i in range(32):
            if n % 2 == 1:
                ones += 1
            n >>= 1
        return ones