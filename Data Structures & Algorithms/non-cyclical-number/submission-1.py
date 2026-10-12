class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def result(num):
            res = 0
            while num > 0:
                digit = num % 10
                res += digit**2
                num //= 10
            return res
        
        num = n
        while True:
            r = result(num)
            if r == 1:
                return True
            elif r in seen:
                return False
            seen.add(r)
            num = r