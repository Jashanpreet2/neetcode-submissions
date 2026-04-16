class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set()
        for num in nums:
            numset.add(num)
        for num in nums:
            if num - 1 not in numset:
                length = 0
                while num in numset:
                    length += 1
                    num += 1
                longest = max(length, longest)
        return longest
        