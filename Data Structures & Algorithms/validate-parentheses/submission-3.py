class Solution:
    def isValid(self, s: str) -> bool:
        p = {"{": "}", "(":")", "[":"]"}
        stack = list()
        i = 0
        while i < len(s):
            while i < len(s) and s[i] in p.keys():
                stack.append(s[i])
                i += 1
            while i < len(s) and s[i] not in p.keys():
                if len(stack) == 0 or s[i] != p[stack[-1]]:
                    return False
                stack.pop()
                i += 1

        return len(stack) == 0