class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        products = [nums[0]] * len(nums)
        negativeProduct =  nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                products[i] = nums[i] * negativeProduct
                negativeProduct = min(nums[i] * products[i-1], nums[i])
            else:
                products[i] = max(nums[i], nums[i] * products[i-1])
                negativeProduct = nums[i] * negativeProduct
            maxProduct = max(maxProduct, products[i])
        return maxProduct        

