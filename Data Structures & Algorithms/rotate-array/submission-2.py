class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate():
            prev = nums[-1]
            for i in range(len(nums)):
                nums[i], prev = prev, nums[i]
        for _ in range(k%len(nums)):
            rotate()