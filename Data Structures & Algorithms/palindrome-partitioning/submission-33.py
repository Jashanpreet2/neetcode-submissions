class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        isPalindromeDict = dict()
        def isPalindrome(start, end):
            if (start, end) in isPalindromeDict:
                return isPalindromeDict[(start, end)]
            if start == end:
                isPalindromeDict[(start, end)] = True
                return True
            if end-start == 1:
                isPalindromeDict[(start, end)] = s[start] == s[end]
                return s[start] == s[end]
            
            isPalindromeDict[(start, end)] = s[start] == s[end] and isPalindrome(start+1, end-1)
            return isPalindromeDict[(start, end)]

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
