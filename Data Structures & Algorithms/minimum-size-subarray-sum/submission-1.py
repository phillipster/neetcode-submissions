from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 1
        min_len = inf if nums[0] < target else 1
        curr = nums[0]
        while right < n:
            curr += nums[right]
            print(f"left: {left}, right: {right}, curr: {curr}")
            while curr >= target:
                if right-left+1 < min_len:
                    min_len = right-left+1
                curr -= nums[left]
                left += 1
            right += 1
        return min_len if min_len < inf else 0
            