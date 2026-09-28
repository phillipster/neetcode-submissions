from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        all_courses = set()
        visiting = set()
        visited = set()
        for pr in prerequisites:
            graph[pr[1]].append(pr[0])
            all_courses.add(pr[0])
            all_courses.add(pr[1])
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for nei in graph[node]:
                ok = dfs(nei)
                if not ok:
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for node in all_courses:
            if node not in visited:
                if not dfs(node):
                    return False
        
        return True
        

