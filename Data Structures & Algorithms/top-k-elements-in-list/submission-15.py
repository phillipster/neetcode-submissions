class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        h = []
        for key, value in counts.items():
            if len(h) == k and value > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (value, key))
            elif len(h) < k:
                heapq.heappush(h, (value, key))
        return [thing[1] for thing in h]