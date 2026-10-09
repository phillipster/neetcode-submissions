class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(grid), len(grid[0])
        q = deque()
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    q.append((i, j))
                    while q:
                        r, c = q.popleft()
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                            grid[r][c] = 0
                            for d in directions:
                                nr, nc = r+d[0], c+d[1]
                                q.append((nr, nc))
        return num_islands
