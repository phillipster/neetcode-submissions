class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        for i in range(n):
            interval = intervals[i]
            if interval[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        res.append(newInterval)  # reached end of list without returning
        return res
