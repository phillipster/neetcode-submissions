class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for num in nums:
            m[num]+=1
        most_frequent, frequency = None, 0
        for key, value in m.items():
            if value > frequency:
                most_frequent, frequency = key, value
        return most_frequent
