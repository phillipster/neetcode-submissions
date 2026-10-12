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
            print(h, cooldown)
            curr = heapq.heappop_max(h)
            if cooldown:
                heapq.heappush_max(h, cooldown)
                cooldown = None
            if curr[0] != 0:
                out.append(curr[1])
                curr[0] -= 1
                cooldown = curr
        if out[-1] == out[-2]: return ''
        return ''.join(out)
        