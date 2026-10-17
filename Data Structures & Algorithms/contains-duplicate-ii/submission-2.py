class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i, val in enumerate(nums):
            if val not in m:
                m[val] = i
            else:
                if i-m[val] <= k:
                    return True
                m[val] = i
        return False