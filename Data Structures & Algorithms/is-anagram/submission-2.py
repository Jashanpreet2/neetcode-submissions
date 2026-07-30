class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = dict()
        for i in range(len(s)):
            if s[i] not in sc:
                sc[s[i]] = 0
            sc[s[i]] += 1
        total = len(s)
        for c in t:
            if c not in sc or sc[c] == 0:
                return False
            sc[c] -= 1
            total -= 1
        return total == 0
        