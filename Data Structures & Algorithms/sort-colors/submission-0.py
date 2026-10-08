class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqs = [0,0,0]
        for num in nums:
            freqs[num]+=1
        for i in range(len(nums)):
            if freqs[0] > 0:
                nums[i]=0
                freqs[0]-=1
            elif freqs[1] > 0:
                nums[i]=1
                freqs[1]-=1
            else:
                nums[i]=2
            
        