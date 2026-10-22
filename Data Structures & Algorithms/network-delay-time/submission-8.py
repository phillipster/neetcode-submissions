from math import inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, t in times:
            g[u].append((v, t))
        distances = {i : math.inf for i in range(1, n+1)}
        distances[k] = 0
        q = [(0, k)]
        while q:
            dist, u = heapq.heappop(q)
            for v, w in g[u]:
                if dist > distances[u]:
                    continue
                if distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    heapq.heappush(q, (distances[v], v))
        max_dist = max(distances.values())
        return max_dist if max_dist < inf else -1