

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        i = 1
        perms = [1] * len(s)
        res = 1
        prev = s[0]
        while i < len(s):
            c = s[i]
            if c == "0" and (prev == "0" or int(prev) > 2):
                return 0
            elif c == "0":
                perms[i] = 1
                perms[i-1] = 1
            elif prev == "0":
                perms[i] = 1
            elif perms[i-1] == 1 and (prev == "1" or (prev =="2" and int(c) <= 6)):
                perms[i] = 2
            elif prev == "1" or (prev == "2" and int(c) <= 6):
                perms[i] = perms[i-1] + perms[i-2]
            prev = c
            if perms[i] <= perms[i-1]:
                res *= perms[i-1]
            i += 1

        return res*perms[-1]
