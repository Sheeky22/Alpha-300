class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        running_min = float('inf')
        best_profit = 0

        for price in prices:

            best_profit = max(best_profit, price - running_min)

            running_min = min(running_min, price)

        return best_profit
