class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts, k = Counter(nums), len(nums)//3
        return [key for key in counts if counts[key] > k]
        '''
        res = []
        n = len(nums)
        m = Counter(nums)
        for key in m:
            if m[key] > n//3:
                res.append(key)
        return res
        '''