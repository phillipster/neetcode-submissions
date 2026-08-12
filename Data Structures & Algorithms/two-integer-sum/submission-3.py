class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = [i]
            else:
                map[nums[i]].append(i)
        for key in map:
            if target-key == key and len(map[key]) == 2:
                return map[key]
            elif target-key in map and target-key != key:
                return map[key] + map[target-key]