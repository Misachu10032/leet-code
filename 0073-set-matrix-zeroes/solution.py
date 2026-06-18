"""
LeetCode 0073 - Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Time:  O(m * n)
Space: O(1)
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0


if __name__ == "__main__":
    sol = Solution()
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(m)
    print(m)  # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(m)
    print(m)  # [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
