class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for elem in nums:
            if elem in map:
                return True
            map[elem] = None
        return False