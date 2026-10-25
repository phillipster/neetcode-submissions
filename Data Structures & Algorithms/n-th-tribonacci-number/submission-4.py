class Solution:
    def tribonacci(self, n: int) -> int:
        T0 = 0
        T1 = 1
        T2 = 1
        if n == 0:
            return T0
        if n == 1 or n == 2:
            return T1
        for i in range(2, n):
            T2, T1, T0 = T2 + T1 + T0, T2, T1
        return T2