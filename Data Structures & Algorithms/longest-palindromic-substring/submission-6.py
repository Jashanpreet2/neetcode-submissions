class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(longest):
                    longest = s[i:j+1]
        return longest