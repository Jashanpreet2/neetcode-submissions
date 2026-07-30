class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = [0] * 26
        for i in range(len(s)):
            sc[ord(s[i])-ord('a')] += 1
        total = len(s)
        for c in t:
            i = ord(c) - ord('a')
            if sc[i] == 0:
                return False
            sc[i] -= 1
            total -= 1
        return total == 0
        