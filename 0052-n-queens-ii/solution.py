"""
LeetCode 0052 - N-Queens II
https://leetcode.com/problems/n-queens-ii/

Time:  O(n!)
Space: O(n)
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diag, anti = set(), set(), set()

        def backtrack(r):
            if r == n:
                return 1
            count = 0
            for c in range(n):
                if c in cols or r - c in diag or r + c in anti:
                    continue
                cols.add(c)
                diag.add(r - c)
                anti.add(r + c)
                count += backtrack(r + 1)
                cols.remove(c)
                diag.remove(r - c)
                anti.remove(r + c)
            return count

        return backtrack(0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNQueens(4))  # 2
    print(sol.totalNQueens(1))  # 1
    print(sol.totalNQueens(8))  # 92
