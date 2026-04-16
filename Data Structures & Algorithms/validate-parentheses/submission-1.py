from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"(": ")", "{": "}", "[": "]"}
        closeToOpen = {")": "(", "}": "{", "]": "["}
        q = deque()
        for bracket in s:
            if bracket in openToClose:
                q.appendleft(bracket)
            else:
                if not len(q) == 0 and openToClose[q[0]] == bracket:
                    q.popleft()
                else:
                    return False
        return len(q) == 0

        