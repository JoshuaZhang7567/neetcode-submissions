class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for day in range(len(prices)-1):
            profit = prices[day+1] - min_buy

            if profit < 0:
                min_buy = prices[day+1]

            else:
                if profit > max_profit:
                    max_profit = profit
                

        return max_profit
            
        