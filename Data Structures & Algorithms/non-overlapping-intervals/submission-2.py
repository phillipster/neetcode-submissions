class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        lastEnd = intervals[0][1]

        for i, (start, end) in enumerate(intervals):
            if i == 0:
                continue
            if lastEnd > start:
                lastEnd = min(end, lastEnd)
                res += 1
            else:
                lastEnd = end
        return res
