class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[-1]:
            beg = 0
            end = len(nums) - 1
        else:
            l = 0
            r = len(nums) - 1
            mid = (l + r) // 2
            beg = mid
            shouldBeSmallerThan = nums[0]
            while l <= r:
                if nums[mid] < shouldBeSmallerThan:
                    beg = mid
                    r = mid - 1
                else:
                    l = mid + 1
                mid = (l + r) // 2
        
            end = beg - 1
        
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        res = -1
        while l <= r:
            currIdx = (beg + mid) % len(nums)
            curr = nums[currIdx]
            if curr == target:
                return currIdx
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2
        return res

        