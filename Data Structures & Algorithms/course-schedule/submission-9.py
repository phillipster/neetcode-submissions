class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # all_nodes = set()
        for v, u in prerequisites:
            graph[u].append(v)
            # all_nodes.add(u)
            # all_nodes.add(v)
        visiting = set()
        visited = set()

        def dfs(u):
            if u in visited:
                return True
            if u in visiting:
                return False
            visiting.add(u)
            for nei in graph[u]:
                if not dfs(nei):
                    return False
            visiting.remove(u)
            visited.add(u)
            return True
            
        for v, u in prerequisites:
            if u not in visited:
                if not dfs(u):
                    return False
        return True
                
