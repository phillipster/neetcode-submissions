class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        arr = [[1],[1,1]]
        for i in range(3, rowIndex+2):
            curr = [1]
            for j in range(1, i-1):
                curr.append(arr[-1][j-1]+arr[-1][j])
            curr.append(1)
            arr.append(curr)
        print(arr)
        return arr[-1]
        
        