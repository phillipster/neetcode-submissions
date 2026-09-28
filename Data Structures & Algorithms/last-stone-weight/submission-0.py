import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = list(stones)
        heapq.heapify_max(h)
        while h:
            if len(h) == 1:
                return h[0]
            s1, s2 = heapq.heappop_max(h), heapq.heappop_max(h)
            if s1 != s2:
                heapq.heappush_max(h, abs(s1-s2))
        return 0
