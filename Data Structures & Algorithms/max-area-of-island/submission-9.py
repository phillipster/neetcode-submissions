class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        max_area = 0

        for a in range(m):
            for b in range(n):
                if grid[a][b] == 1:
                    grid[a][b] = 0
                    q = deque([(a, b)])
                    area = 0
                    while q:
                        i, j = q.popleft()
                        area += 1

                        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                                grid[ni][nj] = 0  # Mark on push, preventing duplicates
                                q.append((ni, nj))
                    if area > max_area:
                        max_area = area

        return max_area