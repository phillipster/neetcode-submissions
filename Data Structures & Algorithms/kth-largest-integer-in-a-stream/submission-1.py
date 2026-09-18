import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = nums
        heapq.heapify(self.data)
        self.capacity = k
        while len(self.data) > k:
            heapq.heappop(self.data)

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        if len(self.data) > self.capacity:
            heapq.heappop(self.data)
        return self.data[0]
