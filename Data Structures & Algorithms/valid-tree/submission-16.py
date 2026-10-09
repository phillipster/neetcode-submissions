class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        graph = defaultdict(set)
        visited = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        def dfs(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei != parent and (nei in visited or not dfs(nei, node)):
                    return False
            return True

        if not dfs(edges[0][0], -1):
            return False
        
        return len(visited) == n

                
        