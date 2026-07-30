class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = dict()
        tc = dict()
        for i in range(len(s)):
            if s[i] not in sc:
                sc[s[i]] = 0
            if t[i] not in tc:
                tc[t[i]] = 0
            sc[s[i]] += 1
            tc[t[i]] += 1
        
        for c in sc:
            if c not in tc or sc[c] != tc[c]:
                return False
        return True
        