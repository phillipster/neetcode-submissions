class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        h = [(value, key) for key, value in counts.items()]
        heapq.heapify_max(h)
        out = []
        for i in range(k):
            out.append(heapq.heappop_max(h)[1])
        return out