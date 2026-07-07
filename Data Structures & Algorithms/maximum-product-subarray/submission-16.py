class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest = nums[0]
        high, low = nums[0], nums[0]
        for n in nums[1:]:
            high, low = max(high*n, low*n, n), min(high*n, low*n, n)
            highest = max(highest, high)
        return highest        

