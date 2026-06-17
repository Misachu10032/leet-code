# 0048. Rotate Image

**Difficulty:** Medium
**Topics:** Array, Math, Matrix
**Link:** https://leetcode.com/problems/rotate-image/

## Approach

Rotate 90 degrees clockwise = transpose, then reverse each row.

## Complexity

- Time: O(n^2)
- Space: O(1)

## Follow-ups / gotchas

- Counter-clockwise: transpose then reverse each column (or reverse rows first).
- Only swap j > i in the transpose or you undo it.
