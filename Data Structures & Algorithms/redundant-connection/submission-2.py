class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # we have one more edge than should be the case for a tree
        parent = [i for i in range(n+1)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x1, y1 = find(x), find(y)
            if x1 == y1:
                return False
            else:
                parent[x1] = y1
                return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
