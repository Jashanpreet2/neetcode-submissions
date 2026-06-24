class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 1
        bits = 0
        while i <= n:
            if i & n:
                bits += 1
            i *= 2
        return bits