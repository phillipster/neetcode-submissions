class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        felipe = set()
        for item in nums:
            if item not in felipe:
                felipe.add(item)
            else:
                return True
        return False