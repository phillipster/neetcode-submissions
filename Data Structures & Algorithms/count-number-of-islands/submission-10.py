class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        num_islands = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    num_islands += 1
                    s = [(x, y)]
                    while s:
                        i, j = s.pop()
                        if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                            grid[i][j] = '0'
                            for d in directions:
                                s.append((i+d[0], j+d[1]))
        
        return num_islands


