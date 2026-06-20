class Solution:
    def rob(self, nums: List[int]) -> int:
        d = dict()
        def recurse(i):
            if i >= len(nums):
                return 0
            if i in d:
                return d[i]
            d[i] = nums[i] + max(recurse(i+2), recurse(i+3))
            return d[i]
        return max(recurse(0), recurse(1))
