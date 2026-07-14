"""
LeetCode 0130 - Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Time:  O(m * n)
Space: O(m * n)
"""


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def mark(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                    board[r][c] = "S"
                    stack.extend(((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)))

        for r in range(rows):
            mark(r, 0)
            mark(r, cols - 1)
        for c in range(cols):
            mark(0, c)
            mark(rows - 1, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


if __name__ == "__main__":
    sol = Solution()
    board = [list('XXXX'), list('XOOX'), list('XXOX'), list('XOXX')]
    sol.solve(board)
    print([''.join(row) for row in board])  # ['XXXX', 'XXXX', 'XXXX', 'XOXX']
