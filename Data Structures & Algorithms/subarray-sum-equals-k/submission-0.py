class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0 : 1}
        count = curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            count += m.get(diff, 0)
            m[curr_sum] = 1 + m.get(curr_sum, 0)
        return count