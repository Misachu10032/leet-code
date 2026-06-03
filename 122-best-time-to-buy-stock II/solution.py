class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i] <buy:
                buy= prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] -buy
        return profit


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = -math.inf
        cash = 0

        for price in prices:
            prev_hold = hold
            hold = max(prev_hold, cash - price)
            cash = max(cash, prev_hold + price)

        return cash