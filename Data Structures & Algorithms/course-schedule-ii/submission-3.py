class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for v, u in prerequisites:
            g[u].append(v)
        res = []
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for nei in g[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            visiting.remove(node)
            visited.add(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]
            