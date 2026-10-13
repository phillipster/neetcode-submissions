from math import inf

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        ans = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(ans, nums[l])
            mid = (l + r) // 2
            if nums[mid] < ans:
                ans = nums[mid]
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return ans
            
