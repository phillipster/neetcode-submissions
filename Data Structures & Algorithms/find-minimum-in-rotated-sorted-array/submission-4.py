class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest_so_far = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            smallest_so_far = min(smallest_so_far, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        return smallest_so_far