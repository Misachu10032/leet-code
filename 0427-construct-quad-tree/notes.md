# 0427. Construct Quad Tree

**Difficulty:** Medium
**Topics:** Array, Divide and Conquer, Tree, Matrix
**Link:** https://leetcode.com/problems/construct-quad-tree/

## Approach

Divide and conquer: if the square is uniform make a leaf, else split into 4 quadrants and recurse.

## Complexity

- Time: O(n^2 log n)
- Space: O(log n)

## Follow-ups / gotchas

- O(n^2) version: build the 4 children first and merge them if all are leaves with the same value.
- Non-leaf val can be anything.
