from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            buy = min(prices[i], buy)
            profit = max(prices[i] - buy, profit)

        return profit
