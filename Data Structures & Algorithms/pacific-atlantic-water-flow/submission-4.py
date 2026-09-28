from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, v):
            v.add((x, y))
            for d in directions:
                i, j = x+d[0], y+d[1]
                if (i, j) not in v and 0 <= i < m and 0 <= j < n \
                                    and heights[i][j] >= heights[x][y]:
                    dfs(i, j, v)
        
        v_p, v_a = set(), set()
        for i in range(m):
            if (i, 0) not in v_p:
                dfs(i, 0, v_p)
            if (i, n-1) not in v_a:
                dfs(i, n-1, v_a)
        for j in range(n):
            if (0, j) not in v_p:
                dfs(0, j, v_p)
            if (m-1, j) not in v_a:
                dfs(m-1, j, v_a)
        
        return list(v_p.intersection(v_a))
        
