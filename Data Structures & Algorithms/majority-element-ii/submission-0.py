class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        m = Counter(nums)
        for key in m:
            if m[key] > n//3:
                res.append(key)
        return res