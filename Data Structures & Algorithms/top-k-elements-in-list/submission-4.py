class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        count_list = [(nums_map[num], num) for num in nums_map]
        count_list.sort()
        count_list.reverse()
        return [count_list[i][1] for i in range(k)]
        