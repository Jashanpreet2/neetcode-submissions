class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        res = x
        power = 1
        while (2 * power) < n:
            res *= res
            power *= 2  
        while power < n:
            res *= x
            power += 1          
        return res