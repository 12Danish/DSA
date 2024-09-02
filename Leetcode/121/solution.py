class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0

        while buy < len(prices) - 1 and sell < len(prices):

            if (prices[sell] - prices[buy]) < 0:
                buy += 1
                if buy != sell:
                    continue



            else:
                if (prices[sell] - prices[buy]) > profit:
                    profit = prices[sell] - prices[buy]
            sell += 1

        return profit
