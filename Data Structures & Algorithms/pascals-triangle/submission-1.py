class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return[[1]]
        arr = [[1], [1,1]]
        for i in range(3, numRows+1):
            curr = [1]
            for j in range(1, i-1):
                curr.append(arr[-1][j-1]+arr[-1][j])
            curr.append(1)
            arr.append(curr)
        return arr