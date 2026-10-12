class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str((int(''.join(str(d) for d in digits))+1)))