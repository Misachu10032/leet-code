"""
LeetCode 0909 - Snakes and Ladders
https://leetcode.com/problems/snakes-and-ladders/

Time:  O(n^2)
Space: O(n^2)
"""


from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def cell(square):
            r, c = divmod(square - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        target = n * n
        moves = {1: 0}
        q = deque([1])
        while q:
            cur = q.popleft()
            if cur == target:
                return moves[cur]
            for nxt in range(cur + 1, min(cur + 6, target) + 1):
                row, col = cell(nxt)
                if board[row][col] != -1:
                    nxt = board[row][col]
                if nxt not in moves:
                    moves[nxt] = moves[cur] + 1
                    q.append(nxt)
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))  # 4
    print(sol.snakesAndLadders([[-1, -1], [-1, 3]]))  # 1
