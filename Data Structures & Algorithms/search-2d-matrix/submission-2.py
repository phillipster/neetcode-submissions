class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        def get(addr):
            i, j = addr // n, addr % n
            print(i, j)
            return matrix[i][j]
        while l <= r:
            mid = (l + r) // 2
            val = get(mid)
            if val == target:
                return True
            if val > target:
                r = mid-1
            else:
                l = mid+1
        return False