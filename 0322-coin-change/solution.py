"""
LeetCode 0322 - Coin Change
https://leetcode.com/problems/coin-change/

Time:  O(amount * coins)
Space: O(amount)
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = amount + 1
        dp = [0] + [INF] * amount
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # 3
    print(sol.coinChange([2], 3))  # -1
    print(sol.coinChange([1], 0))  # 0
