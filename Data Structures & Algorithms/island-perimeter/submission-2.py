class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(grid), len(grid[0])
        perimeter = 0
        q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))
                    while q:
                        r, c = q.popleft()
                        # print(r, c)
                        for d in directions:
                            nr, nc = r+d[0], c+d[1]
                            visited.add((nr, nc))
                            if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] == 0:
                                perimeter += 1
                            else:
                                if (nr,nc) not in visited:
                                    q.append((nr, nc))
                            
        return perimeter
