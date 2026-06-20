class Solution:
    def climbStairs(self, n: int) -> int:
        d = dict()
        def recurse(m):
            if m < 0:
                return 0
            if m == 0:
                return 1
            if m in d:
                return d[m]
            d[m] = recurse(m-1) + recurse(m-2)
            return d[m]
        return recurse(n)
        
            