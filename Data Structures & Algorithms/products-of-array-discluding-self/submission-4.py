from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        result = [0] * len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i]
        result[-1] = result[-2]
        m = nums[-1]
        for i in range(len(nums)-2, 0,-1):
            result[i] = m * result[i - 1]
            m *= nums[i]
        result[0] = m
        return result