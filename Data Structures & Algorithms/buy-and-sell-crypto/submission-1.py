class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while buy < sell and sell < len(prices):
            if prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return profit