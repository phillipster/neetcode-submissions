class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        slow, fast = 0, 0
        while fast < len(nums):
            print(slow, nums[fast], seen)
            if nums[fast] not in seen:
                seen.add(nums[fast])
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow