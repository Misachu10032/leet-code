# 0073. Set Matrix Zeroes

**Difficulty:** Medium
**Topics:** Array, Hash Table, Matrix
**Link:** https://leetcode.com/problems/set-matrix-zeroes/

## Approach

Use the first row and first column as marker arrays. Remember separately whether
the first row/column themselves had a zero, and handle them last.

## Complexity

- Time: O(m * n)
- Space: O(1)

## Follow-ups / gotchas

- Easy version: two sets of zero rows/cols, O(m + n) space.
- Don't zero the first row/col before using them as markers.
