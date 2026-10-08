class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        m1 = defaultdict(int)
        for i in range(len(s1)):
            m1[s1[i]] += 1
        m2 = defaultdict(int)
        for i in range(len(s1)):
            m2[s2[i]] += 1
        if m1 == m2:
            return True
        l, r = 0, len(s1)
        while l < r < len(s2):
            if s2[r] not in m1:
                m1[s2[r]] = 0
            if s2[l] not in m1:
                m1[s2[l]] = 0
            m2[s2[l]] -= 1
            m2[s2[r]] += 1
            if m1 == m2:
                return True
            l += 1
            r += 1
        return False
