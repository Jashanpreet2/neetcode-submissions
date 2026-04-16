class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = 0
        for i in range(len(s)):
            characters = set()
            curlong = 0
            for j in range(i, len(s)):
                if s[j] in characters:
                    break
                curlong += 1
                longest = longest if curlong <= longest else curlong
                characters.add(s[j])
        return longest
            