class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            # Compare distance between x and arr[mid] vs x and arr[mid + k]
            # If arr[mid + k] is closer to x than arr[mid], the window must shift right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left : left + k]
        
