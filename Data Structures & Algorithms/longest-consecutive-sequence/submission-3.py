class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set()
        considered = set()
        for num in nums:
            numset.add(num)
        for num in nums:
            length = 0
            if num - 1 not in numset:
                while num in numset:
                    length += 1
                    num += 1
            if length >= longest:
                longest = length
        return longest
        