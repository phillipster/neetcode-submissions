class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest = 0
        left, right = 0, len(heights)-1
        while left < right:
            base = right-left
            area = base * min(heights[left], heights[right])
            if area > greatest:
                greatest = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return greatest