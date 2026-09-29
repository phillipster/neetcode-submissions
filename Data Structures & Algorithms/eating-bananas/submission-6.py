class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        lowest_so_far = max(piles)
        while l <= r:
            mid = (l + r) // 2
            # print(f"l, r, rates[mid] = {l}, {r}, {rates[mid]}")
            hours = sum(math.ceil(p / mid) for p in piles)
            # print(f"hours: {hours}")
            if hours > h:
                l = mid + 1
            else:
                lowest_so_far = min(lowest_so_far, mid)
                r = mid - 1
        return lowest_so_far
        