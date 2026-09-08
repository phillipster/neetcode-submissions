class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for num in nums:
            if num not in numset:
                numset.add(num)
            else:
                return True
        return False