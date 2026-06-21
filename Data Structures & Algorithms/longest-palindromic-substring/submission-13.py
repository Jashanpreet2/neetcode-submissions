class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            beg = i
            end = i
            while beg-1 >= 0 and s[beg-1] == s[i]: beg -= 1
            while end+1 < len(s) and s[end+1] == s[i]: end += 1
            while beg-1 >= 0 and end+1 < len(s) and s[beg-1] == s[end+1]:
                beg -= 1
                end += 1
            if end - beg + 1 > len(longest):
                longest = s[beg:end+1]
        return longest