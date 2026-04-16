class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subset = []
        def add_subsets(i):
            if i == len(nums):
                return
            add_subsets(i+1)
            subset.append(nums[i])
            res.append(subset.copy())
            add_subsets(i+1)
            subset.pop()
        add_subsets(0)
        return res