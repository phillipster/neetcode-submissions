class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        out = [intervals[0]]
        for start, end in intervals:
            lastEnd = out[-1][1]
            if lastEnd > start:
                out[-1][-1] = min(end, lastEnd)
            else:
                out.append([start, end])
        return len(intervals)-len(out)
