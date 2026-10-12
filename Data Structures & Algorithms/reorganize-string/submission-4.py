class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) <= 1: return s
        counts = Counter(s)
        if len(counts) < 2:
            return ''
        out = []
        h = []
        for key, value in counts.items():
            heapq.heappush_max(h, [value, key])
        cooldown = None
        while h:
            curr = heapq.heappop_max(h)
            if cooldown:
                heapq.heappush_max(h, cooldown)
                cooldown = None
            out.append(curr[1])
            curr[0] -= 1
            if curr[0] > 0:
                cooldown = curr
        return ''.join(out) if len(out) == len(s) else ''
        