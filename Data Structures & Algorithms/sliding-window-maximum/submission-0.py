class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0, len(nums) - k + 1):
            largest = nums[i]
            j = 1
            while j < k:
                if nums[i+j] > largest:
                    largest = nums[i+j]
                j += 1
            res.append(largest)
        return res