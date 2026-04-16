from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = None
        zeros = 0
        for num in nums:
            if num != 0:
                if product_all == None:
                    product_all = num
                else:
                    product_all *= num
            else:
                zeros += 1
        if zeros == 1:
            return [0 if num != 0 else product_all for num in nums]
        if zeros >= 2:
            return [0] * len(nums)
        return [product_all // num if num != 0 else product_all for num in nums]