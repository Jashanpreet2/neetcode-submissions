class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for num in range(n+1):
            i=1
            while i <= num:
                if num & i:
                    res[num] += 1
                i *= 2
        return res
        