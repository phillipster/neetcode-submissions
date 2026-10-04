class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right, n = 0, 0, len(nums)
        while right < n:
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return left