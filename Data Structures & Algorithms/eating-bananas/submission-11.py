from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return None
        
        def valid(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            if hours <= h:
                return True
            return False
        
        l, r = 1, max(piles)
        best = r

        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                best = min(best, mid)
                r = mid-1
            else:
                l = mid + 1
        
        return best