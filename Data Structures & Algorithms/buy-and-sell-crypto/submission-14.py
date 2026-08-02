class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cheapest = prices[0]
        for price in prices:
            res = max(price - cheapest, res)
            cheapest = min(cheapest, price)

        return res
