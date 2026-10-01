class Solution:
    def tribonacci(self, n: int) -> int:
        if 0 <= n <= 2:
            return 0 if n == 0 else 1
        n3, n2, n1 = 1, 1, 0
        for i in range(3, n+1):
            next_num = n3 + n2 + n1
            n1, n2, n3 = n2, n3, next_num
        return n3