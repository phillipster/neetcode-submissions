class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        m = defaultdict(int)
        for num in nums:
            m[num] = m[num-1] + 1
        return max(m.values())
                