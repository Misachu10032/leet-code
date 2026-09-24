"""
LeetCode 0063 - Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

Time:  O(m * n)
Space: O(n)
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(sol.uniquePathsWithObstacles([[0, 1], [0, 0]]))  # 1
    print(sol.uniquePathsWithObstacles([[1]]))  # 0
