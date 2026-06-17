"""
LeetCode 0048 - Rotate Image
https://leetcode.com/problems/rotate-image/

Time:  O(n^2)
Space: O(1)
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    sol = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(m)
    print(m)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
