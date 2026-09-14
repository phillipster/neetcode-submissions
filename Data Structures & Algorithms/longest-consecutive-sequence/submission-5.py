class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        max_len = 1
        for num in nums:
            if num-1 not in numset:
                cur = 1
                while num+1 in numset:
                    cur += 1
                    num += 1
                if cur > max_len:
                    max_len = cur
        return max_len