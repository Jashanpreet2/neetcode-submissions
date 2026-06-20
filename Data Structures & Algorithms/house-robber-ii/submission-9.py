class Solution:
    def rob(self, nums: List[int]) -> int:
        d = dict()
        d["withlast"] = dict()
        d["nolast"] = dict()
        def recurse(i, last):
            if i >= len(nums) or (i == len(nums) - 1 and (not last) and len(nums) > 1):
                return 0
            if i in d["withlast"]:
                return d["withlast"][i] if last else d["nolast"][i]
            d["withlast"][i] = nums[i] + max(recurse(i+2, True), recurse(i+3, True))
            d["nolast"][i] = nums[i] + max(recurse(i+2, False), recurse(i+3, False))
            return d["withlast"][i] if last else d["nolast"][i]
        return max(recurse(0, False), recurse(1, True), recurse(2, True))
        