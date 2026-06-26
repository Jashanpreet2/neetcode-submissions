class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            if n & 1:
                res ^= 1
            res <<= 1
            n >>= 1
        res >>= 1
        return res