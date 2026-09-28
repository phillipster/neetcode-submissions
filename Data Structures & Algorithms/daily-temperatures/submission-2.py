class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n
        s = []
        for i in range(n):
            t = temperatures[i]
            while s and s[-1][0] < t:
                sT, sIdx = s.pop()
                output[sIdx] = i - sIdx
            s.append((t, i))
        return output