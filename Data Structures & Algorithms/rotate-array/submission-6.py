class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = [n for n in nums]
        k = k%len(nums)
        for i in range(len(nums)):
            nums[i] = copy[i-k]