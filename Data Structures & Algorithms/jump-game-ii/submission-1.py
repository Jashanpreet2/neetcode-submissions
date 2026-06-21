class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 1
        cur = 1
        maxReachable = nums[0]
        while maxReachable < len(nums)-1:
            curReachable = maxReachable
            while cur <= maxReachable:
                curReachable = max(curReachable, cur+nums[cur])
                cur += 1
            maxReachable = curReachable
            jumps += 1
        return jumps

        