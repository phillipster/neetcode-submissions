class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            out = []
            i = j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    out.append(arr1[i])
                    i += 1
                else:
                    out.append(arr2[j])
                    j += 1
            while i < len(arr1):
                out.append(arr1[i])
                i += 1
            while j < len(arr2):
                out.append(arr2[j])
                j += 1
            return out

        def sort(arr):
            n = len(arr)
            if n == 0:
                return []
            if n == 1:
                return arr
            left = sort(arr[:n//2])
            right = sort(arr[n//2:])
            return merge(left, right)

        return sort(nums)
            