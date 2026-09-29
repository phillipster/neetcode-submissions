class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def p(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = p(x * x, n // 2)
            return x * res if n % 2 else res
        if n < 0:
            return 1 / p(x, -n)
        else:
            return p(x, n)