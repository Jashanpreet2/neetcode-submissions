class Solution:
    def isValid(self, s: str) -> bool:
        otoc = {'(':')', '{':'}', '[':']'}
        ctoo = {')':'(', '}':'{', ']':'['}
        stack = []
        for b in s:
            if b in ctoo:
                if len(stack) == 0 or ctoo[b] != stack[-1]:
                    return False
                stack.pop()
                continue
            stack.append(b)
        return len(stack) == 0
        