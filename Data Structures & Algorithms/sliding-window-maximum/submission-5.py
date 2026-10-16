class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_vals = []
        q = deque()
        i, j = 0, 0
        
        while j < len(nums):
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)
            if i > q[0]:
                q.popleft()
            
            if (j+1) >= k:
                max_vals.append(nums[q[0]])
                i += 1
            j += 1
        
        return max_vals

