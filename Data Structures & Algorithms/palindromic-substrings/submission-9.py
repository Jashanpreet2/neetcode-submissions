import math
class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        i,left,right=0,0,0
        while i < len(s):
            skipTo = i+1
            left, right, n = i-1, i+1, 1
            while left >= 0 and s[left] == s[i]:
                left -=1
                n+=1
            while right < len(s) and s[right] == s[i]: 
                skipTo += 1
                right += 1
                n+=1
            
            # n/1 + n/2 + n/3 +...  n/n
            # (1+2+3+...+n)/1*2*3*n
            total += (n*n+n)//2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left-1, right+1
                total += 1
            i += 1
            i = skipTo
            print(i, right)
            
        return total