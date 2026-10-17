class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = defaultdict(set)
        for i, val in enumerate(nums):
            if val not in m:
                m[val].add(i)
            else:
                for j in range(k+1):
                    if i-j in m[val]:
                        return True
                m[val].add(i)
        print(m)
        return False