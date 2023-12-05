class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - curr_min <= 0:
                curr_min = prices[i]
            else:
                profit = max(profit, prices[i] - curr_min)
        return profit
