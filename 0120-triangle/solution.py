"""
LeetCode 0120 - Triangle
https://leetcode.com/problems/triangle/

Time:  O(n^2)
Space: O(n)
"""


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(row + 1):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
    print(sol.minimumTotal([[-10]]))  # -10
