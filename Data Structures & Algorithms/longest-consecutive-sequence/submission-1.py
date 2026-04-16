class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        longest =  1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr += 1
                if curr > longest:
                    longest = curr
            elif nums[i] != nums[i - 1]:
                curr = 1
        return longest
            
        