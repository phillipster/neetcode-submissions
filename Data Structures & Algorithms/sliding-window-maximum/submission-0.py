from sortedcontainers import SortedDict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_vals = []
        window = SortedDict()
        for n in nums[:k]:
            if n not in window:
                window[n] = 1
            else:
                window[n] += 1
        max_vals.append(max(window))
        i, j = 0, k
        while j < len(nums):
            # print(f"arr: {nums[i:j]}")
            if window[nums[i]] > 1:
                window[nums[i]] -= 1
            else:
                del window[nums[i]]
            if nums[j] not in window:
                window[nums[j]] = 1
            else:
                window[nums[j]] += 1
            max_vals.append(max(window))
            i +=1
            j += 1
        return max_vals
