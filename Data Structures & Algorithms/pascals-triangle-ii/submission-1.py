class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        q = deque([[1],[1,1]])
        for i in range(3, rowIndex+2):
            curr = [1]
            for j in range(1, i-1):
                curr.append(q[-1][j-1]+q[-1][j])
            curr.append(1)
            q.append(curr)
            q.popleft()
        print(q)
        return q[-1]
        
        