from math import inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        all_nodes = set()
        for u, v, t in times:
            g[u].append((v, t))
            all_nodes.add(u)
            all_nodes.add(v)
        if len(all_nodes) < n:
            return -1
        distances = {node : inf for node in all_nodes}
        distances[k] = 0
        q = [(0, k)]
        while q:
            dist, u = heapq.heappop(q)
            for v, w in g[u]:
                if distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    heapq.heappush(q, (distances[v], v))
        max_dist = max(distances.values())
        return max_dist if max_dist < inf else -1