class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = 0
        e = len(s) - 1
        while b <= e:
            if not s[b].isalnum():
                b += 1
                continue
            if not s[e].isalnum():
                e -= 1
                continue
            if s[b].lower() != s[e].lower():
                return False
            b += 1
            e -= 1
        return True