# 0074. Search a 2D Matrix

**Difficulty:** Medium
**Topics:** Array, Binary Search, Matrix
**Link:** https://leetcode.com/problems/search-a-2d-matrix/

## Approach

The matrix is one sorted array split into rows. Binary search over 0..m*n-1 and map
index -> (index // cols, index % cols).

## Complexity

- Time: O(log(m * n))
- Space: O(1)

## Follow-ups / gotchas

- Divide by cols, not rows.
- For 240 (rows and cols sorted separately) start from the top-right corner instead.
