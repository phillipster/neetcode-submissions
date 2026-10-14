class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        max_area = 0

        for a in range(m):
            for b in range(n):
                if grid[a][b] == 1:
                    q = deque([(a, b)])
                    area = 0
                    while q:
                        i, j = q.popleft()
                        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                            area += 1
                            grid[i][j] = 0
                            for x, y in directions:
                                q.append((i+x, j+y))
                    if area > max_area:
                        max_area = area

        return max_area