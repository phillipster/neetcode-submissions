class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        def valid(mid):
            i = count = 0
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= mid:
                    count += 1
                    i += 1
                i += 1
                if count == p:
                    return True
            return False

        nums.sort()
        m = 1000000001
        l, r = 0, m
        last_valid = m-1
        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                last_valid = mid
                r = mid-1
            else:
                l = mid+1
        return last_valid
            
