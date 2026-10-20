class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        for c in s1:
            count_s1[c] += 1
        
        need = len(count_s1)
        for i in range(len(s2)):
            count_s2, cur = defaultdict(int), 0
            for j in range(i, len(s2)):
                count_s2[s2[j]] += 1
                if count_s1[s2[j]] < count_s2[s2[j]]:
                    break
                if count_s1[s2[j]] == count_s2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False