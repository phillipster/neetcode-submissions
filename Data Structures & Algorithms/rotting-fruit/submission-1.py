from collections import deque
from math import inf

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        num_fresh = 0
        num_rotten = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    q.append((i, j))
                    visited.add((i, j))
                    num_rotten += 1
                else:
                    num_fresh += 1
        for row in grid:
            print(row)
        layer = 1
        while q:
            x, y = q.popleft()
            for d in directions:
                print(f"Layer: {layer}")
                i, j = x+d[0], y+d[1]
                if 0 <= i < m and 0 <= j < n \
                        and grid[i][j] != -1 and (i, j) not in visited:
                    grid[i][j] = grid[x][y]+1
                    visited.add((i,j))
                    q.append((i, j))
            layer += 1
        print(f"Num rotten: {num_rotten}, num fresh: {num_fresh}, len(visited): {len(visited)}")
        for row in grid:
            print(row)
        if len(visited) - num_rotten != num_fresh:
            return -1
        
        largest = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > largest:
                    largest = grid[i][j]
        return largest
