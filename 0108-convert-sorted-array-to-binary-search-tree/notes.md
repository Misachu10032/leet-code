# 0108. Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy
**Topics:** Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
**Link:** https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

## Approach

Pick the middle element as root so both halves are equal size, recurse on each half.

## Complexity

- Time: O(n)
- Space: O(log n)

## Follow-ups / gotchas

- Pass indices instead of slicing to stay O(n).
- Either middle works for even lengths.
