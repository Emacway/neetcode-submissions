class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers solution

        i = 0 #sell day
        j = 1 #buy day

        maxP = 0 #initialize

        while j < len(prices):
            if prices[i] < prices[j]: #we have a profit!
                profit = prices[j] - prices[i]
                if profit > maxP:
                    maxP = profit
            else:
                i = j #we found a cheaper buy price!
            j += 1
        
        return maxP
        

