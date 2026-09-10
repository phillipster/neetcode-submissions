class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights)-1
        while l < r:
            w = r - l
            area = max(area, min(heights[l], heights[r]) * w)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area
