from math import inf

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        s = []

        leftMostBar = [-1] * n
        for i in range(n):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                leftMostBar[i] = s[-1]
            s.append(i)

        print(leftMostBar)
        
        s = []

        rightMostBar = [n] * n
        for i in range(n-1, -1, -1):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                rightMostBar[i] = s[-1]
            s.append(i)

        maxArea = 0
        for i in range(n):
            leftMostBar[i] += 1
            rightMostBar[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMostBar[i] - leftMostBar[i] + 1))
        return maxArea



