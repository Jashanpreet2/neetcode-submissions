class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = nums[0]
        i = 0
        while i < len(nums) and i <= maxReachable:
            maxReachable = max(maxReachable, i+nums[i])
            i += 1
        return maxReachable >= len(nums)-1