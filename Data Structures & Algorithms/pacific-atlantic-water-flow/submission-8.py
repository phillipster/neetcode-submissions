class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def bfs(q, s):
            while q:
                a, b = q.popleft()
                for ai, bi in directions:
                    r, c = a + ai, b + bi
                    if 0 <= r < m and 0 <= c < n and (r, c) not in s \
                    and heights[r][c] >= heights[a][b]:
                        s.add((r, c))
                        q.append((r, c))
        
        m, n = len(heights), len(heights[0])
        q1, q2 = deque(), deque()
        for i in range(m):
            q1.append((i, 0))
            q2.append((i, n-1))
        for j in range(n):
            q1.append((0, j))
            q2.append((m-1, j))
        pacific = set(q1)
        atlantic = set(q2)
        
        bfs(q1, pacific)    
        bfs(q2, atlantic)

        return [list(pair) for pair in pacific.intersection(atlantic)]
        

