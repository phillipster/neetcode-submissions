class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        # Below: solution for n*log(n)
        # pairs_by_freq = [(counts[key], key) for key in counts]
        # pairs_by_freq.sort(reverse=True)
        # out = []
        # for i in range(k):
        #     out.append(pairs_by_freq[i][1])
        # return out
        # Now, bucket sort:
        freq = [[] for _ in range(len(nums) + 1)]
        for key in counts.keys():
            freq[counts[key]].append(key)
        out = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                out.append(num)
                if len(out) == k:
                    return out