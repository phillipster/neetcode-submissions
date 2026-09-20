from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        if not edges:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(parent, node):
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return True  # leaf node
            passed = True
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                if not dfs(node, neighbor):
                    passed = False
            return passed

        return dfs(None, next(iter(graph))) and len(visited) == n-1
            

        
