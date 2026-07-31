class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cheapest, j = prices[0], 1
        while j < len(prices):
            curCheap = prices[j]
            while j+1 < len(prices) and prices[j+1] > prices[j]:
                j += 1
                curCheap = min(curCheap, prices[j])
            cheapest = min(cheapest, curCheap)
            res = max(res, prices[j]-cheapest)
            j += 1
        return res
