"""
LeetCode 0123 - Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))  # 6
    print(sol.maxProfit([1, 2, 3, 4, 5]))  # 4
    print(sol.maxProfit([7, 6, 4, 3, 1]))  # 0
