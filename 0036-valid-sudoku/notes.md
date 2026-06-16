# 0036. Valid Sudoku

**Difficulty:** Medium
**Topics:** Array, Hash Table, Matrix
**Link:** https://leetcode.com/problems/valid-sudoku/

## Approach

One pass with a seen-set per row, column and 3x3 box. Box index = (r // 3) * 3 + c // 3.

## Complexity

- Time: O(1) (81 cells)
- Space: O(1)

## Follow-ups / gotchas

- Only validate filled cells; the board doesn't need to be solvable.
