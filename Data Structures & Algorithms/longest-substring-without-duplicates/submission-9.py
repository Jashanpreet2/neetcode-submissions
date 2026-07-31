class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        beg, end = 0, 0
        seen = set()
        res = 0

        while end < len(s):
            while s[end] in seen:
                seen.remove(s[beg])
                beg += 1
    
            seen.add(s[end])
            res = max(res, end-beg+1)
            end += 1

        return res
            