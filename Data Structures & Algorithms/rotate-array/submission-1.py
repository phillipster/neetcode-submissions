class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        out = nums[k:] + nums[:k]
        nums.clear()
        nums.extend(out)
        nums.reverse()
        

        