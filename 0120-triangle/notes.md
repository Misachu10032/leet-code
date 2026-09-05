# 0120. Triangle

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming
**Link:** https://leetcode.com/problems/triangle/

## Approach

Bottom-up: start from the last row and fold each row upward, taking the cheaper of the two children.
The top ends up holding the answer.

## Complexity

- Time: O(n^2)
- Space: O(n)

## Follow-ups / gotchas

- Bottom-up avoids edge handling for the triangle's sides.
- One row of extra space meets the O(n) follow-up.
