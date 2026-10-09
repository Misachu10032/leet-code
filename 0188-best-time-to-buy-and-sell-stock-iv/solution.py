"""
LeetCode 0188 - Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Time:  O(n * k)
Space: O(k)
"""


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for t in range(1, k + 1):
                buy[t] = max(buy[t], sell[t - 1] - price)
                sell[t] = max(sell[t], buy[t] + price)
        return sell[k]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2, [2, 4, 1]))  # 2
    print(sol.maxProfit(2, [3, 2, 6, 5, 0, 3]))  # 7
