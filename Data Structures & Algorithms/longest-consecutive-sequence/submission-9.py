class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        maxlen = 0
        while len(s) > 0:
            num = s.pop()
            curlen = 1
            cur = num
            while cur - 1 in s:
                cur -= 1
                s.remove(cur)
                curlen += 1
            cur = num
            while cur + 1 in s:
                cur += 1
                s.remove(cur)
                curlen += 1
            maxlen = max(maxlen, curlen)
        return maxlen

        