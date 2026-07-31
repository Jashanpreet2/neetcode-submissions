class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i, j = 0, 1
        while j < len(prices):
            nextI = j
            while j+1 < len(prices) and prices[j+1] > prices[j]:
                j += 1
                nextI = nextI if prices[nextI] < prices[j] else j
            i = i if prices[i] < prices[nextI] else nextI
            res = max(res, prices[j]-prices[i])
            j += 1
        return res
