class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) solution

        maxProfit = 0

        for i in range(1, len(prices)):
            # Let i be the index for the SELLING price

            # the optimal BUYING price is the minimum to the left of index i
            buyingPrices = prices[:i]
            bestBuyingPrice = min(buyingPrices)

            profit = prices[i] - bestBuyingPrice

            if profit > maxProfit:
                maxProfit = profit
            
        
        return maxProfit