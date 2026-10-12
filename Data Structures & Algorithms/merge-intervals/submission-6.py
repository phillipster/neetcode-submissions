class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for interval in intervals:
            lastEnd = output[-1][1]
            if interval[0] <= lastEnd:
                output[-1][-1] = max(interval[1], lastEnd)
            else:
                output.append(interval)

        return output