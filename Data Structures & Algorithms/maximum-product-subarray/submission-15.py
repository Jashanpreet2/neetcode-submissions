class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest = nums[0]
        high, low = nums[0], nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            high, low = max(high*n, low*n, n), min(high*n, low*n, n)
            highest = max(highest, high)
        return highest        

