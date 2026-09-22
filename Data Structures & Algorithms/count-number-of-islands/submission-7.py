from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands, m, n = 0, len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    q.append((i,j))
                    while q:
                        i, j = q.popleft()
                        if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                            grid[i][j] = '0'
                            q.append((i+1, j))
                            q.append((i-1, j))
                            q.append((i, j+1))
                            q.append((i, j-1))
        return num_islands
            