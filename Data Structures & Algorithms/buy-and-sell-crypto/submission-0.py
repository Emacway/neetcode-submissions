class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        # initialize two pointers
        #i = 0 #left
        #j = len(prices) - 1 #right

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                buyPrice = prices[i]
                sellPrice = prices[j]

                profit = sellPrice - buyPrice

                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
