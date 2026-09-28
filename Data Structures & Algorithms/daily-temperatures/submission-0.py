class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        s = []
        for i in range(n):
            while s and temperatures[i] > s[-1][0]:
                temp, idx = s.pop()
                output[idx] = i - idx
            s.append((temperatures[i], i))
        return output