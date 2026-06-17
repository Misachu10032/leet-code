# 0054. Spiral Matrix

**Difficulty:** Medium
**Topics:** Array, Matrix, Simulation
**Link:** https://leetcode.com/problems/spiral-matrix/

## Approach

Keep four boundaries and peel layers: top row, right column, bottom row, left column, shrinking each time.

## Complexity

- Time: O(m * n)
- Space: O(1) extra

## Follow-ups / gotchas

- Re-check top <= bottom and left <= right before the bottom/left passes, or a single row/col gets added twice.
