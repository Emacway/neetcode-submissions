class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2) solution
        maxProfit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                buyPrice = prices[i]
                sellPrice = prices[j]

                profit = sellPrice - buyPrice

                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
