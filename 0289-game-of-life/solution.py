"""
LeetCode 0289 - Game of Life
https://leetcode.com/problems/game-of-life/

Time:  O(m * n)
Space: O(1)
"""


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                live = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if (dr or dc) and 0 <= r + dr < m and 0 <= c + dc < n:
                            live += board[r + dr][c + dc] & 1
                if board[r][c] & 1 and live in (2, 3):
                    board[r][c] |= 2
                elif not board[r][c] & 1 and live == 3:
                    board[r][c] |= 2
        for r in range(m):
            for c in range(n):
                board[r][c] >>= 1


if __name__ == "__main__":
    sol = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.gameOfLife(board)
    print(board)  # [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
