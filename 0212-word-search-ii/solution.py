"""
LeetCode 0212 - Word Search II
https://leetcode.com/problems/word-search-ii/

Time:  O(m * n * 4^L)
Space: O(total characters)
"""


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word

        rows, cols = len(board), len(board[0])
        found = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent[ch]
            word = node.pop("$", None)
            if word:
                found.append(word)
            board[r][c] = "#"
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node:
                    dfs(nr, nc, node)
            board[r][c] = ch
            if not node:
                parent.pop(ch)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
        return found


if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.findWords([list('oaan'), list('etae'), list('ihkr'), list('iflv')], ['oath', 'pea', 'eat', 'rain'])))  # ['eat', 'oath']
    print(sol.findWords([list('ab'), list('cd')], ['abcb']))  # []
