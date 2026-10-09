class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = 0
            for d in directions:
                r, c = i+d[0], j+d[1]
                if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                    dfs(r, c)
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands
