# 0221. Maximal Square

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Matrix
**Link:** https://leetcode.com/problems/maximal-square/

## Approach

dp[i][j] = side of the largest square with bottom-right corner at (i, j)
= 1 + min(top, left, top-left) when the cell is '1'. Rolled into one row, saving the diagonal.

## Complexity

- Time: O(m * n)
- Space: O(n)

## Follow-ups / gotchas

- Return the area, not the side.
- Matrix holds strings '0'/'1'.
