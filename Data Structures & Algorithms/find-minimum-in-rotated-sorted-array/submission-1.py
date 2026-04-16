class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        res = mid
        shouldBeSmallerThan = nums[0]
        while l <= r:
            if nums[mid] < shouldBeSmallerThan:
                res = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r) // 2
        
        return res
