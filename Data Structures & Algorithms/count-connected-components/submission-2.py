from collections import defaultdict

class Solution:
    # this is just count number of islands, but funny
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        num_connected = 0
        for node in graph:
            if node not in visited:
                num_connected += 1
                dfs(node)
        if n > len(visited):
            num_connected += abs(n-len(visited))
        return num_connected