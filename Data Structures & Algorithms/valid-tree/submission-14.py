class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        graph = defaultdict(set)
        all_nodes = set()
        visiting = set()
        visited = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            all_nodes.add(u)
            all_nodes.add(v)
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for nei in graph[node]:
                graph[nei].remove(node)
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        if not dfs(edges[0][0]) or len(visited) < len(all_nodes):
            return False
        return True