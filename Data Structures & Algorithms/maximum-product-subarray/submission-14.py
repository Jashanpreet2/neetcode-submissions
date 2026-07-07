class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = nums[0]
        negativeProduct =  nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                product, negativeProduct = nums[i] * negativeProduct, min(nums[i] * product, nums[i])
            else:
                product, negativeProduct = max(nums[i], nums[i] * product), nums[i] * negativeProduct
            maxProduct = max(maxProduct, product)
        return maxProduct        

