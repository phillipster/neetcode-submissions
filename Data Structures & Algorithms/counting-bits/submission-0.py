class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]*(n+1)
        for j in range(0, n+1):
            x = j
            ones = 0
            for i in range(32):
                if x % 2 == 1:
                    ones += 1
                x >>= 1
            out[j] = ones
        return out
        
