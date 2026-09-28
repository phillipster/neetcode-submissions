# from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            x, y = p
            d = math.sqrt((x)**2+(y)**2)
            if len(h) == k:
                heapq.heappushpop_max(h, (d, p))
            else:
                heapq.heappush_max(h, (d, p))
        return [item[1] for item in h]
