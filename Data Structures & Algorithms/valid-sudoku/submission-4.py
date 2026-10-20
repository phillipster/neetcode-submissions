class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            counts = [0] * n
            for j in range(n):
                num = board[i][j]
                if num == '.': continue
                num = int(num)
                if counts[num-1] == 1:
                    return False
                counts[num-1] = 1
        for j in range(n):
            counts = [0] * n
            for i in range(n):
                num = board[i][j]
                if num == '.': continue
                num = int(num)
                if counts[int(num-1)] == 1:
                    return False
                counts[num-1] = 1
        for k in range(9):
            counts = [0] * n
            for i in range(3):
                for j in range(3):
                    row = (k // 3) * 3 + i
                    col = (k % 3) * 3 + j
                    num = board[row][col]
                    if num == '.': continue
                    num = int(num)
                    if counts[num-1] == 1:
                        return False
                    counts[num-1] = 1
        return True