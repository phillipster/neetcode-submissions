from collections import defaultdict
from math import inf
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        all_nodes = set()
        graph = defaultdict(list)
        visited = set()
        for u, v, w in times:
            graph[u].append((v, w))
            all_nodes.add(u)
            all_nodes.add(v)
        distances = {node : inf for node in all_nodes}
        distances[k] = 0
        q = [(0, k)]

        while q:
            dist, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            if dist <= distances[node]:
                for nei, weight in graph[node]:
                    dist_through_curr = dist + weight
                    if dist_through_curr < distances[nei]:
                        distances[nei] = dist_through_curr
                        heapq.heappush(q, (dist_through_curr, nei))

        res = max(distances.values())
        return res if res != inf and len(visited) == n else -1