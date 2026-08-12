class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addr = {}
        for i in range(len(nums)):
            addr[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in addr and i != addr[target-nums[i]]:
                return [i, addr[target-nums[i]]]
 