class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        products = [nums[0]] * len(nums)
        negativeProducts = [nums[0]] * len(nums)
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                negativeProducts[i] = min(nums[i] * products[i-1], nums[i])
                products[i] = nums[i] * negativeProducts[i-1]
            else:
                products[i] = max(nums[i], nums[i] * products[i-1])
                negativeProducts[i] = nums[i] * negativeProducts[i-1]
            maxProduct = max(maxProduct, products[i])
        return maxProduct        

