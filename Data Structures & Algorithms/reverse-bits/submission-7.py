class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n > 0:
            if n & 1:
                res ^= 1
            n >>= 1
            i += 1
            if n == 0:
                break
            res <<= 1
        res <<= max(0, 32-i)
        return res