class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[nums[i], i] for i in range(len(nums))]
        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            num1, num2 = nums[i][0], nums[j][0]
            if num1 + num2 < target:
                i += 1
            elif num1 + num2 > target:
                j -= 1
            else:
                return [min(nums[i][1], nums[j][1]), max(nums[i][1], nums[j][1])]