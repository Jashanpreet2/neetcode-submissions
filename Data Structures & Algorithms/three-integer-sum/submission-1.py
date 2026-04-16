class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        a = 0
        nums.sort()

        while a < len(nums):
            if a > 0 and nums[a] == nums[a-1]:
                a += 1
                continue
            if a == len(nums) - 2:
                return triplets
            s1 = a + 1
            s2 = len(nums) - 1
            while s1 < s2:
                total = nums[a] + nums[s1] + nums[s2]
                if total == 0:
                    triplets.append([nums[a], nums[s1], nums[s2]])
                    s1 += 1
                    while s1 < s2 and nums[s1] == nums[s1-1]:
                        s1 += 1
                elif total < 0:
                    s1 += 1
                else:
                    s2 -= 1
            a += 1
        return triplets