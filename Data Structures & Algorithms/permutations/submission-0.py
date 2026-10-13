class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = [[]]
        
        for num in nums:
            next_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    next_perms.append(p[:i] + [num] + p[i:])
            perms = next_perms
            
        return perms