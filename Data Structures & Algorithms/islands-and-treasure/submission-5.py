class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        while q:
            r, c = q.popleft()
            for i, j in directions:
                a, b = r+i, c+j
                if 0 <= a <= m-1 and 0 <= b <= n-1 and grid[a][b] == 2147483647:
                    grid[a][b] = grid[r][c] + 1
                    q.append((a, b))
            
