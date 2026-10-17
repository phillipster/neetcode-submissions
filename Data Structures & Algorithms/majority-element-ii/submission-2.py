class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts, k = Counter(nums), len(nums)//3
        return [key for key in counts if counts[key] > k]