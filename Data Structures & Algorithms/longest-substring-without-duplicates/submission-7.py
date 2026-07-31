class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        beg, end = 0, 0
        seen = set()
        res = 0
        while end < len(s):
            c1, c2 = s[beg], s[end]
            if c2 not in seen:
                seen.add(c2)
                res = max(res, end-beg+1)
                end += 1
            else:
                beg += 1
                seen.remove(c1)
        return res
            