class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        isPalindromeDict = dict()
        def isPalindrome(start, end):
            if (start, end) in isPalindromeDict:
                return isPalindromeDict[(start, end)]
            length = end-start+1
            if length%2 == 1:
                lo = hi = start+(length // 2)
            else:
                lo = start+(length // 2 - 1) 
                hi = lo + 1
            while lo >= start:
                if s[lo] != s[hi]:
                    isPalindromeDict[(start, end)] = False
                    return False
                lo -= 1
                hi += 1
            isPalindromeDict[(start, end)] = True
            return True

        def backtrack(cur, start):
            if start == len(s):
                res.append(cur.copy())
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    cur.append(s[start:i+1])
                    backtrack(cur, i+1)
                    cur.pop()

        backtrack([], 0)
        return res
