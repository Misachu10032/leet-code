"""
LeetCode 0221 - Maximal Square
https://leetcode.com/problems/maximal-square/

Time:  O(m * n)
Space: O(n)
"""


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n = len(matrix[0])
        dp = [0] * (n + 1)
        best = 0
        for row in matrix:
            prev_diag = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if row[j - 1] == "1":
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev_diag)
                    best = max(best, dp[j])
                else:
                    dp[j] = 0
                prev_diag = temp
        return best * best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalSquare([list('10100'), list('10111'), list('11111'), list('10010')]))  # 4
    print(sol.maximalSquare([list('01'), list('10')]))  # 1
    print(sol.maximalSquare([list('0')]))  # 0
