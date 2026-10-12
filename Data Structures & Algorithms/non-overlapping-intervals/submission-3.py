class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if lastEnd > start:
                lastEnd = min(end, lastEnd)
                res += 1
            else:
                lastEnd = end
        return res
