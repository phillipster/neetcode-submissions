class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        def dac(arr):
            if len(arr) < 1:
                return None
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            left_merge = dac(arr[:mid])
            right_merge = dac(arr[mid:])
            if not left_merge:
                return right_merge
            if not right_merge:
                return left_merge
            merge_idx = 0
            while merge_idx < len(right_merge) and left_merge[-1][1] >= right_merge[merge_idx][0]:
                left_merge[-1] = [min(left_merge[-1][0], right_merge[merge_idx][0]),
                                    max(left_merge[-1][1], right_merge[merge_idx][1])]  
                merge_idx += 1
            res = left_merge + right_merge[merge_idx:]
            return res
        return dac(intervals)