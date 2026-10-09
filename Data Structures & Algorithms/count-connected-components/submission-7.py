class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        visited = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei, node)
        
        num_connected = 0
        for edge in edges:
            if edge[0] not in visited:
                num_connected += 1
                dfs(edge[0], -1)
        
        return num_connected + abs(n-len(visited))