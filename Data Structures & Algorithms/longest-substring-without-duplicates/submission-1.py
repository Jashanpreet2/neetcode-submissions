class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = 1
        i = 0
        j = 0
        chars = set()
        while j < len(s):
            while s[j] in chars:
                if s[i] in chars:
                    chars.remove(s[i])
                i += 1
            length = j - i + 1
            longest = length if length > longest else longest
            chars.add(s[j])
            j += 1

        return longest