class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        pairs_by_freq = [(counts[key], key) for key in counts]
        pairs_by_freq.sort(reverse=True)
        out = []
        for i in range(k):
            out.append(pairs_by_freq[i][1])
        return out