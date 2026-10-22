class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * (n)
        s = []
        
        for i, temp in enumerate(temperatures):
            while s and temp > temperatures[s[-1]]:
                unresolved_idx = s.pop()
                answer[unresolved_idx] = i-unresolved_idx
            
            s.append(i)
        
        return answer