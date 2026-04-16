class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_so_far = {}
        for i, num in enumerate(nums):
            if target - num in nums_so_far:
                return [nums_so_far[target - num], i]
            nums_so_far[num] = i
            
