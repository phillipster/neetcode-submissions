import copy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # grid = copy.deepcopy(grid)
        def dfs(grid, i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[i])) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
        
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    n += 1
                    dfs(grid, i, j)
        return n