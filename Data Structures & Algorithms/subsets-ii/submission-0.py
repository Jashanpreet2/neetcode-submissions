class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        cur = []
        indices = []
        def backtrack(i):
            if i >= len(nums):
                return
            cur.append(nums[i])
            indices.append(i)
            res.append(cur.copy())
            backtrack(i+1)
            cur.pop()
            indices.pop()
            j = i+1
            while j < len(nums) and nums[j] == nums[i]: j += 1
            backtrack(j)
        backtrack(0)
        return res
        
        