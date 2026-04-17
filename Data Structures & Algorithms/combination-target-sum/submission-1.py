class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(i, cursum):
            if i >= len(nums) or nums[i] > target:
                return
            if nums[i] + cursum > target:
                backtrack(i+1, cursum)
                return
            frequency_added = (target-cursum)//nums[i]
            stack.extend([nums[i]] * frequency_added)
            cursum += frequency_added * nums[i]
            if cursum == target:
                res.append(stack.copy())
            while frequency_added > 0:
                backtrack(i+1, cursum)
                stack.pop()
                frequency_added -= 1
                cursum -= nums[i]
                if len(stack) == 0:
                    break
            backtrack(i+1, cursum)
        backtrack(0, 0)
        return res
        