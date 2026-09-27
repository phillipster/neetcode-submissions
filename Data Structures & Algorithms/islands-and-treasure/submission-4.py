from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            for d1, d2 in directions:
                if (0 <= i+d1 < m and 0 <= j+d2 < n and grid[i+d1][j+d2] > grid[i][j]+1):
                    grid[i+d1][j+d2] = grid[i][j]+1
                    q.append((i+d1, j+d2))
            
                
               

