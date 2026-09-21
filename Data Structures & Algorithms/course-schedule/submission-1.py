from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        all_nodes = set()
        visiting = set()  # gray
        visited = set()  # black
        for u, v in prerequisites:
            graph[v].append(u)
            all_nodes.update((u, v))
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        for node in all_nodes:
            if node not in visited and not dfs(node):
                return False
            visited.add(node)
        return True