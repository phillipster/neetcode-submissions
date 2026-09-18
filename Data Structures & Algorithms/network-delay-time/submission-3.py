from collections import defaultdict
from math import inf
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distances = {node: inf for node in range(1, n + 1)}
        distances[k] = 0
        q = [(0, k)]

        while q:
            dist, node = heapq.heappop(q)
            if dist <= distances[node]:
                for nei, weight in graph[node]:
                    dist_through_curr = dist + weight
                    if dist_through_curr < distances[nei]:
                        distances[nei] = dist_through_curr
                        heapq.heappush(q, (dist_through_curr, nei))

        res = max(distances.values())
        return res if res != inf else -1