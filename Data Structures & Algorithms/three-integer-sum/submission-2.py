class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        prev_num = None
        for k in range(len(nums)):
            if nums[k] == prev_num:
                continue
            l, r = k+1, len(nums)-1
            while l < r:
                cur = nums[k] + nums[l] + nums[r]
                if cur == 0 and k != l != r:
                    result.append((nums[k], nums[l], nums[r]))
                if cur < 0:
                    l += 1
                else:
                    r -= 1
            prev_num = nums[k]
        return list(set(result))