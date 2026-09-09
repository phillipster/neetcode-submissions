class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
    
        def dfs(i, j):
            if (
                not (0 <= i < len(grid) and 0 <= j < len(grid[i]))
                or ((i,j) in visited)
                or grid[i][j] == '0'
            ):
                return
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    n += 1
                    dfs(i, j)
        return n