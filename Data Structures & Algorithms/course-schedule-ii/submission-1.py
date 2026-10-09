class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for v, u in prerequisites:
            graph[u].append(v)
        visiting = set()
        visited = set()
        output = []

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            output.append(node)
            visiting.remove(node)
            visited.add(node)
            return True
        for v, u in prerequisites:
            if not dfs(u):
                return []
        for i in range(numCourses):
            if i not in visited:
                output.append(i)
        return output[::-1]
        