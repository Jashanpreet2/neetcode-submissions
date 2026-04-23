class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numset = nums.copy()
        res = []
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(numset)):
                if numset[i] != None:
                    num = numset[i]
                    numset[i] = None
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
                    numset[i] = num
        backtrack([])
        return res
