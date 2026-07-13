"""
LeetCode 0200 - Number of Islands
https://leetcode.com/problems/number-of-islands/

Time:  O(m * n)
Space: O(m * n)
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def sink(r, c):
            stack = [(r, c)]
            grid[r][c] = "0"
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    sink(r, c)
        return islands


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([list('11110'), list('11010'), list('11000'), list('00000')]))  # 1
    print(sol.numIslands([list('11000'), list('11000'), list('00100'), list('00011')]))  # 3
