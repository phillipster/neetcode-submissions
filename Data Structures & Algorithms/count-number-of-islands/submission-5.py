class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands, m, n = 0, len(grid), len(grid[0])
        def dfs(i, j):
            s = []
            s.append((i,j))
            while s:
                i, j = s.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                    grid[i][j] = '0'
                    s.append((i+1, j))
                    s.append((i-1, j))
                    s.append((i, j+1))
                    s.append((i, j-1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands
            