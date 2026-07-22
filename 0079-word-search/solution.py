"""
LeetCode 0079 - Word Search
https://leetcode.com/problems/word-search/

Time:  O(m * n * 3^L)
Space: O(L)
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                     or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    sol = Solution()
    board = [list('ABCE'), list('SFCS'), list('ADEE')]
    print(sol.exist(board, 'ABCCED'))  # True
    print(sol.exist(board, 'SEE'))  # True
    print(sol.exist(board, 'ABCB'))  # False
