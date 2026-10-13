class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        out = []
        sub = []
        
        def bt(i):
            if len(sub) == len(nums):
                out.append(sub[:])
                return 
            else:
                for j in range(len(nums)):
                    if nums[j] in sub:
                        continue
                    sub.append(nums[j])
                    bt(j + 1)
                    sub.pop()
        bt(0)
        return out