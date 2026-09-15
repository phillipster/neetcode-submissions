from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        
        def bfs(i, j):
            q = deque()
            grid[i][j] = 0
            q.append((i, j))
            res = 1

            while q:
                cell = q.popleft()
                for direction in directions:
                    x, y = cell[0] + direction[0], cell[1] + direction[1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        q.append((x, y))
                        grid[x][y] = 0
                        res += 1
            
            return res

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = max(result, bfs(i, j))
        return result