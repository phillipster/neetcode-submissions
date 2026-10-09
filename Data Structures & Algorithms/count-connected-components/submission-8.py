class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
                    
        num_components = 0
        
        for i in range(n):
            if i not in visited:
                num_components += 1
                dfs(i)
                
        return num_components