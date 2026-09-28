class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(x, y):
            visited.add((x, y))
            for dir in directions:
                i, j = x+dir[0], y+dir[1]
                if (i, j) not in visited and 0 <= i < m and 0 <= j < n \
                        and board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(1, m-1):
            if (i, 0) not in visited and board[i][0] == 'O':
                dfs(i, 0)
            if (i, n-1) not in visited and board[i][n-1] == 'O':
                dfs(i, n-1)
        for j in range(1, n-1):
            if (0, j) not in visited and board[0][j] == 'O':
                dfs(0, j)
            if (m-1, j) not in visited and board[m-1][j] == 'O':
                dfs(m-1, j)
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if (i, j) not in visited:
                    board[i][j] = 'X'
