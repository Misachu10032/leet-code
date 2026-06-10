# 0006. Zigzag Conversion

**Difficulty:** Medium
**Topics:** String
**Link:** https://leetcode.com/problems/zigzag-conversion/

## Approach

Simulate: walk down then up the rows, appending each char to its row. Join rows at the end.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- numRows == 1 would bounce forever between the same row, so return early.
