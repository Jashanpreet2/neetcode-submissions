class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = 0
        e = len(s) - 1
        while b <= e:
            while b < len(s) and not s[b].isalnum():
                b += 1
            while e >= 0 and not s[e].isalnum():
                e -= 1
            if b >= len(s) or e < 0:
                return True
            if s[b].lower() != s[e].lower():
                return False
            b += 1
            e -= 1
        return True