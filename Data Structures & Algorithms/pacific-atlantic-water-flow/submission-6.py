class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def bfs(q, s):
            while q:
                a, b = q.popleft()
                s.add((a, b))
                for ai, bi in directions:
                    r, c = a + ai, b + bi
                    if 0 <= r < m and 0 <= c < n and (r, c) not in s \
                    and heights[r][c] >= heights[a][b]:
                        q.append((r, c))
        
        m, n = len(heights), len(heights[0])
        q = deque()
        for i in range(m):
            q.append((i, 0))
        for j in range(n):
            q.append((0, j))
        pacific = set(q)
        bfs(q, pacific)
        
        for i in range(m):
            q.append((i, n-1))
        for j in range(n):
            q.append((m-1, j))
        atlantic = set(q)
        bfs(q, atlantic)

        return [list(pair) for pair in pacific.intersection(atlantic)]
        

