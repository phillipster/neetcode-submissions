class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            q = deque()
            q.append((i, j))
            while q:
                r, c = q.pop()
                grid[r][c] = 0
                for d in directions:
                    nr, nc = r+d[0], c+d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        q.append((nr, nc))

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands
