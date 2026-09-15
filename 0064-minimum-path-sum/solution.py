"""
LeetCode 0064 - Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Time:  O(m * n)
Space: O(n)
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        dp = [float("inf")] * n
        dp[0] = 0
        for row in grid:
            dp[0] += row[0]
            for j in range(1, n):
                dp[j] = row[j] + min(dp[j], dp[j - 1])
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]))  # 12
