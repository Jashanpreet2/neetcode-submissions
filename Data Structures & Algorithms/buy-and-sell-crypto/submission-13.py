class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cheapest = prices[0]

        for p in prices:
            cheapest = min(cheapest, p)
            res = max(res, p - cheapest)

        return res
