class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dir in directions:
                        r, c = i+dir[0], j+dir[1]
                        if not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0:
                            perimeter += 1
        return perimeter
