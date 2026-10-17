from math import inf

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(num for num in nums if num >= 0)
        num = 1
        while num in s:
            num += 1
        return num
        