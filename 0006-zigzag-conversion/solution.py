"""
LeetCode 0006 - Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        row, step = 0, 1
        for ch in s:
            rows[row] += ch
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join(rows)


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert('PAYPALISHIRING', 3))  # PAHNAPLSIIGYIR
    print(sol.convert('PAYPALISHIRING', 4))  # PINALSIGYAHRPI
